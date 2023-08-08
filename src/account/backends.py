from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.backends import ModelBackend
from .models import CustomUser


class UserRoleBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = CustomUser.objects.get(username=username)
            if user.check_password(password) and user.role == "company":
                return user
            elif user.check_password(password) and user.role == "employee":
                return user
            # elif user.check_password(password) and user.role == 'admin':
            #     return user
        except CustomUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None


class CustomUserBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = super().authenticate(
            request, username=username, password=password, **kwargs
        )
        if user and not user.is_active:
            # User account is not active, return None to prevent login
            return None
        return user
