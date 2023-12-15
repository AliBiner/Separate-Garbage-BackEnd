from rest_framework import request
from rest_framework.generics import CreateAPIView
from user.models import User
from user.api.serializers import UserCreateSerializer,UserLoginSerializer

class UserLoginAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer

class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer




