
from django.urls import path

from user.api.views import UserCreateAPIView, UserLoginAPIView

app_name = 'user'
urlpatterns = [
    path('create/', UserCreateAPIView.as_view(), name='create'),
    path('login/', UserLoginAPIView.as_view(), name='login')
]