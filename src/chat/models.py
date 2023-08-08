from django.db import models
import uuid
from django.contrib.auth import get_user_model
from config.models.TimeStampMixin import TimeStampMixin


class Room(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Message(TimeStampMixin):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True, max_length=36
    )
    # room = models.ForeignKey(Room, on_delete=models.CASCADE)
    sender = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="sender"
    )
    receiver = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="reveiver"
    )
    content = models.TextField()

    def __str__(self):
        return self.content
