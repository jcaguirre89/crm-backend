from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    AllowAny,
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

from .serializers import UserSerializer


User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    """
    `list`, `create`, `retrieve`, `update` and `destroy` actions for
    the User model.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CheckLogin(APIView):
    """
    Check if User with given Token exists
    """

    allowed_methods = ["POST"]
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        try:
            token = Token.objects.get(key=request.data)
            return Response({"authenticated": True}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({"authenticated": False}, status=status.HTTP_403_FORBIDDEN)
