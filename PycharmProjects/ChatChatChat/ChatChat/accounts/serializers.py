from rest_framework import serializers

from .models import User


class UserNicknameSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id")


class AuthorizedUsers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "nickname")

    def get_queryset(self):
        queryset = User.objects.filter(auth_token__isnull=True)

        return queryset


