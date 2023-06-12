import os

from django.conf import settings
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from PIL import Image
from accounts.models import User


class UserProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request):
        user = request.user
        data = {
            'nickname': user.nickname,
            'avatar': user.avatar.url if user.avatar else None
        }
        return Response(data)

    def put(self, request):
        nickname = request.data.get('nickname')
        avatar = request.FILES.get('avatar')

        user = request.user

        if nickname:
            user.nickname = nickname

        if avatar:
            user.avatar = avatar

        user.save()

        data = {
            'message': 'User profile updated successfully',
            'nickname': user.nickname,
            'avatar': user.avatar.url
        }
        return Response(data)


class AuthorizedUsersView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        authorized_users = User.objects.filter(auth_token__isnull=False)
        user_list = [(user.id, user.nickname) for user in authorized_users]
        return Response({'authorized_users': user_list})
