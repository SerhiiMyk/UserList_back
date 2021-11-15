from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.users.models import UserModel
from apps.users.serializers import UserSerializer


class UserListCreateView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
