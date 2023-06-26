from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, renderer_classes
from .models import CustomUser


@api_view(['GET'])
@renderer_classes([JSONRenderer])  # Specify the renderer class
def activate_account(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = CustomUser.objects.get(pk=uid)
        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            response_data = {
                'message': 'Account activated successfully'
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            response_data = {
                'message': 'Invalid activation token'
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        response_data = {
            'message': 'Invalid activation link'
        }
        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

