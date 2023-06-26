from django.urls import path
from .views import register_user


urlpatterns = [
    path('create-user/', register_user, name='create-user-view'),
]