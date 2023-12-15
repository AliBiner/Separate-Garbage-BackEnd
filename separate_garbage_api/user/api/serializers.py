from django.db.models import Q
from django.contrib.auth.password_validation import validate_password
from django.core.validators import EmailValidator, MinLengthValidator, MaxLengthValidator
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.validators import UniqueValidator
from user.models import User


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[EmailValidator]
    )
    password = serializers.CharField(required=True, style={'input_type': 'password'})

    name = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = [
            'email',
            'password',
            'name',
        ]

    def create(self, validated_data):

        email = validated_data.get('email')
        password = validated_data.get('password')
        response_user = User.objects.get(Q(email=email), Q(password=password))

        if response_user is None:
            raise serializers.ValidationError('Geçersiz Kullanıcı Adı veya Şifre')
        else:
            return response_user

    def to_representation(self, response_user):
        return {'deneme': response_user.id, 'name': response_user.name}


class UserCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all()), EmailValidator]
    )
    password = serializers.CharField(validators=[validate_password, MinLengthValidator(8), MaxLengthValidator(50)])
    rePassword = serializers.CharField(validators=[validate_password])

    class Meta:
        model = User
        fields = [
            'name',
            'surname',
            'email',
            'password',
            'rePassword',
        ]

    def validate(self, attrs):

        if attrs['password'] != attrs['rePassword']:
            raise serializers.ValidationError('Passwords do not match')
        return attrs

    def create(self, validated_data):
        if self.is_valid():
            user = User.objects.create(
                name=validated_data['name'],
                surname=validated_data['surname'],
                email=validated_data['email'],
                password=validated_data['password']
            )
            user.save()
            return Response(data=self.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=self.errors, status=status.HTTP_400_BAD_REQUEST)
