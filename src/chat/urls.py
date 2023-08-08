from django.urls import include, path
from rest_framework import routers
from .views import RoomViewSet, MessageViewSet, PersonalMessageViewSet


router = routers.DefaultRouter()
router.register(r"rooms", RoomViewSet)
router.register(r"messages", MessageViewSet)
router.register(r"my-messages", PersonalMessageViewSet, basename="personal-message")

urlpatterns = [
    path("", include(router.urls)),
]
