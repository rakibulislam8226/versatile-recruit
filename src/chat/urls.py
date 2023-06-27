from django.urls import include, path
from rest_framework import routers
from .views import RoomViewSet, MessageViewSet


router = routers.DefaultRouter()
router.register(r'rooms', RoomViewSet)
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
