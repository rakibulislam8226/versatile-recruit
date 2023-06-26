from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth.hashers import make_password

from .serializers import CustomUserSerializer


@swagger_auto_schema(method='post', request_body=CustomUserSerializer)
@api_view(['POST'])
def register_user(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        validated_data = serializer.validated_data
        password = validated_data['password']
        hashed_password = make_password(password)  # Hash the password
        validated_data['password'] = hashed_password
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

