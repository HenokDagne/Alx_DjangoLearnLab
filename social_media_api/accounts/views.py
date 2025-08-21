from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .models import CustomUser
from rest_framework import serializers

# Serializers
class RegisterSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)

	class Meta:
		model = CustomUser
		fields = ('username', 'email', 'password', 'bio', 'profile_picture')

	def create(self, validated_data):
		user = CustomUser.objects.create_user(
			username=validated_data['username'],
			email=validated_data.get('email', ''),
			password=validated_data['password'],
			bio=validated_data.get('bio', ''),
			profile_picture=validated_data.get('profile_picture', None)
		)
		return user

class LoginSerializer(serializers.Serializer):
	username = serializers.CharField()
	password = serializers.CharField(write_only=True)

	def validate(self, data):
		user = authenticate(username=data['username'], password=data['password'])
		if user and user.is_active:
			return user
		raise serializers.ValidationError("Invalid credentials")

class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomUser
		fields = ('id', 'username', 'email', 'bio', 'profile_picture', 'followers', 'following')

# Views
class RegisterView(generics.CreateAPIView):
	queryset = CustomUser.objects.all()
	serializer_class = RegisterSerializer
	permission_classes = [AllowAny]

	def create(self, request, *args, **kwargs):
		response = super().create(request, *args, **kwargs)
		user = CustomUser.objects.get(username=response.data['username'])
		token, created = Token.objects.get_or_create(user=user)
		response.data['token'] = token.key
		return response

class LoginView(APIView):
	permission_classes = [AllowAny]

	def post(self, request):
		serializer = LoginSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data
		token, created = Token.objects.get_or_create(user=user)
		return Response({'token': token.key})

class ProfileView(generics.RetrieveUpdateAPIView):
	queryset = CustomUser.objects.all()
	serializer_class = ProfileSerializer
	permission_classes = [IsAuthenticated]

	def get_object(self):
		return self.request.user


