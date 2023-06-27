from django.urls import path
from .views import register_user, LoginAPI, LogoutAPI
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .activation import activate


urlpatterns = [
    path('create-user/', register_user, name='create-user-view'),
    path('activate/<str:uidb64>/<str:token>/', activate, name='activate'),

    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', LogoutAPI.as_view(), name='logout'),

    path('get-token/', TokenObtainPairView.as_view(), name='get-token'),
    path('token-refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('token-verify/', TokenVerifyView.as_view(), name='oken-verify'),
]