from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.urls import reverse
import secrets



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
    is_active = models.BooleanField(default=False)
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
    activation_token = models.CharField(max_length=255, blank=True)

    def generate_activation_token(self):
        self.activation_token = secrets.token_urlsafe(32)
        self.save()

    def send_activation_email(self, request):
        current_site = get_current_site(request)
        token_generator = default_token_generator
        
        # Generate the activation token
        token = token_generator.make_token(self)
        
        # Generate the uidb64 for the user's primary key
        uidb64 = urlsafe_base64_encode(force_bytes(self.pk))
        
        # Construct the activation link
        activation_url = reverse('activate', kwargs={'uidb64': uidb64, 'token': token})
        activation_link = f"http://{current_site.domain}{activation_url}"
        
        mail_subject = 'Activate your account'
        message = render_to_string(
            'activation_email.html',
            {
                'user': self,
                'activation_link': activation_link,
            }
        )
        email = EmailMessage(mail_subject, message, to=[self.email])
        email.send()



    def save(self, *args, **kwargs):
        if not self.pk:  # Only for newly created users
            self.is_active = False
        super().save(*args, **kwargs)
