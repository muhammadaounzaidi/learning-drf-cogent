from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from users.api.serializers import RegisterSerializer


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data = request.data)

        if serializer.is_valid(raise_exception = True):
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            response = Response(
                {
                    "user": {
                        "email": user.email,
                    },
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                },
                status = status.HTTP_201_CREATED,
            )
        else:
            response = Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        return response
