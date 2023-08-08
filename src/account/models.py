from django.db import models
from django.contrib.auth.models import AbstractUser
from django_q.tasks import async_task
from .choices import ROLE_CHOICES
import secrets


class CustomUser(AbstractUser):
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=15)
    website = models.URLField(blank=True, null=True)  # TODO: use it only for company
    is_active = models.BooleanField(default=False)
    # Add unique related_name for groups field
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_set",
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
        verbose_name="groups",
    )

    # Add unique related_name for user_permissions field
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_set",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )
    activation_token = models.CharField(max_length=255, blank=True)

    def generate_activation_token(self):
        self.activation_token = secrets.token_urlsafe(32)
        self.save()

    def send_activation_email(self, domain):
        async_task("account.tasks.send_activation_email_async", self.id, domain)

    def save(self, *args, **kwargs):
        if not self.pk:  # Only for newly created users
            self.is_active = False
        super().save(*args, **kwargs)
