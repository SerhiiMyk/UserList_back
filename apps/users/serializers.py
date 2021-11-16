from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.users.models import UserModel


class UserSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        exclude = ('last_login',)

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data: dict):
        user = UserModel.objects.create_user(**validated_data)
        return user

    def validate(self, data):
        user_type = data.get('user_type')
        if user_type != 'Admin' and user_type != 'Driver':
            raise serializers.ValidationError('user type must be Admin or Driver')
        return data
