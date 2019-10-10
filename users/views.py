from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from users.models import User
from users.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    `list`, `create`, `retrieve`, `update` and `destroy` actions for
    the User model.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

