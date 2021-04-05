from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.password_validation import validate_password
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, permissions
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.viewsets import mixins
from rest_framework.authtoken.serializers import AuthTokenSerializer

from auth_api.models import User
from auth_api.serializers import UserAuthSignUpSerializer, UserAuthSignInSerializer, UserAuthOutputSerializer, \
    UserSerializer


class UserViewSet(GenericViewSet, mixins.ListModelMixin):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="current_user_read", responses={200: UserSerializer()},
    )
    def list(self, request, *args, **kwargs):
        return Response(self.serializer_class(self.request.user, context={"request": request}).data)


class AuthViewSet(GenericViewSet):
    serializer_class = UserAuthOutputSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(request_body=UserAuthSignInSerializer)
    @action(methods=["POST"], detail=False)
    def sign_in(self, request, *args, **kwargs):
        data = request.data
        try:
            user = authenticate(request, email=data["email"], password=data["password"], )
        except get_user_model().DoesNotExist:
            raise ValidationError("This user does not exist")
        except KeyError:
            raise ValidationError("Enter your email address")

        if not user:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(self.serializer_class(user, context={"request": request}).data)

    @swagger_auto_schema(request_body=UserAuthSignUpSerializer)
    @action(methods=["POST"], detail=False)
    def sign_up(self, request, *args, **kwargs):
        serializer = UserAuthSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = User(
            username=serializer.validated_data["email"],
            email=serializer.validated_data["email"],
            first_name=serializer.validated_data["first_name"],
            last_name=serializer.validated_data["last_name"],
        )

        try:
            validate_password(serializer.validated_data["password"], user=user)
        except ValidationError as e:
            return Response(data=e, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(serializer.validated_data["password"])
        user.save()

        return Response(self.serializer_class(user, context={"request": request}).data)

