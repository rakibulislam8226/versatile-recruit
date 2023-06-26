from django.urls import path
from .views import register_user, LoginAPI, LogoutAPI
from .activation import activate_account


urlpatterns = [
    path('create-user/', register_user, name='create-user-view'),
    path('activate/<str:uidb64>/<str:token>/', activate_account, name='activate'),

    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', LogoutAPI.as_view(), name='logout'),
]