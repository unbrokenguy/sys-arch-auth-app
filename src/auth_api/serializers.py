from rest_framework import serializers
from rest_framework.authtoken.models import Token as AuthToken

from auth_api.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    User model serializer.
    """
    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
        )

        extra_kwargs = {"email": {"read_only": True, }}


class UserAuthOutputSerializer(UserSerializer):
    """
    User model serializer with auth_token field.
    """
    auth_token = serializers.SerializerMethodField()

    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + ("auth_token",)

    def get_auth_token(self, obj):
        token, created = AuthToken.objects.get_or_create(user=obj)
        return token.key


class UserAuthSignInSerializer(serializers.ModelSerializer):
    """
    Sign in data serializer.
    """
    class Meta:
        model = User
        fields = ("email", "password")


class UserAuthSignUpSerializer(serializers.ModelSerializer):
    """
    Sign up data serializer.
    """
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password")
        extra_kwargs = {
            "email": {"required": True},
            "password": {"required": True},
            "first_name": {"required": True},
            "last_name": {"required": True},
        }


