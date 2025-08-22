from rest_framework import generics, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from .models import CustomUser
from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from notifications.views import create_notification



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





class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        target_user = get_object_or_404(CustomUser, pk=pk)
        if target_user == request.user:
            return Response({"detail": "You cannot follow yourself"}, status=status.HTTP_400_BAD_REQUEST)
        request.user.following.add(target_user)
        target_user.followers.add(request.user)
        create_notification(
            recipient=target_user,
            actor=request.user,
            verb="started following you",
            target=request.user,
            is_read=True
        )
        return Response({"detail": f"You are now following {target_user.username}"}, status=status.HTTP_200_OK)

class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk):
        target_user = get_object_or_404(CustomUser, pk=pk)
        if target_user == request.user:
            return Response({"detail": "You cannot unfollow yourself"}, status=status.HTTP_400_BAD_REQUEST)
        request.user.following.remove(target_user)
        target_user.followers.remove(request.user)
        create_notification(
            recipient=target_user,
            actor=request.user,
            verb="stopped following you",
            target=request.user,
            is_read=True
        )
        return Response({"detail": f"You have unfollowed {target_user.username}"}, status=status.HTTP_200_OK)