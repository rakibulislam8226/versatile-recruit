from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, views, response, status
from .models import Room, Message
from .serializers import RoomSerializer, MessageSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)


class PersonalMessageViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        messages = Message.objects.filter(receiver=request.user)
        serializer = MessageSerializer(messages, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)
