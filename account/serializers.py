from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Permission, Group, update_last_login
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.serializers import TokenRefreshSerializer, TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.state import token_backend

from account.models import ClubUser


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    groups_id = serializers.SerializerMethodField()
    groups_name = serializers.SerializerMethodField()
    permissions_name = serializers.SerializerMethodField()
    url_path = serializers.SerializerMethodField()
    avatar = serializers.ImageField()
    password = serializers.CharField(
        write_only=True,
        required=False,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = ClubUser
        fields = "__all__"
        read_only_field = ['is_active', 'created', 'updated', 'created_at']
        extra_kwargs = {
            'groups': {'write_only': True},
        }

    @staticmethod
    def get_permissions_name(obj):
        return [perm.name for perm in obj.user_permissions.all()]

    @staticmethod
    def get_groups_name(obj):
        return [group.name for group in obj.groups.all()]

    @staticmethod
    def get_groups_id(obj):
        return [group.id for group in obj.groups.all()]

    @staticmethod
    def get_url_path(obj):
        return obj.photo_url

    @staticmethod
    def get_avatar(obj):
        return obj.avatar

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name', 'permissions']


class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        data = super(CustomTokenRefreshSerializer, self).validate(attrs)
        decoded_payload = token_backend.decode(data['access'], verify=True)
        user_uid = decoded_payload['user_id']
        # add filter query

        obj = get_object_or_404(ClubUser, pk=user_uid)
        data['user'] = UserSerializer(obj).data
        groups = []
        perms = []
        for group in obj.groups.all():
            groups.append(group.name)
            for perm in group.permissions.all():
                perms.append(perm.codename)
            for perm in obj.user_permissions.all():
                perms.append(perm.codename)
        perms = tuple(perms)
        data.update({'groups_name': groups, "permissions_name": perms})
        return data


class LoginSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['user'] = UserSerializer(self.user).data
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data


class RegisterSerializer(UserSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)
    email = serializers.EmailField(required=True, write_only=True, max_length=128)

    class Meta:
        model = ClubUser
        fields = ['first_name', 'last_name', 'id', 'username', 'email', 'password', 'is_active', 'created_at']

    def create(self, validated_data):
        try:
            user = ClubUser.objects.get(email=validated_data['email'])
        except ObjectDoesNotExist:
            user = ClubUser.objects.create_user(**validated_data)
        return user
