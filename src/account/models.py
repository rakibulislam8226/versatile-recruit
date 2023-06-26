from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('company', 'Comapany'),
        ('employee', 'Employee'),
        # ('admin', 'Admin'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=15)
    website = models.URLField(blank=True, null=True)
    # Add unique related_name for groups field
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )

    # Add unique related_name for user_permissions field
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def save(self, *args, **kwargs):
        # If the user's role is not company, clear the website field
        if self.role != 'company':
            self.website = None
        super().save(*args, **kwargs)
