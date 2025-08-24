from rest_framework.permissions import IsAuthenticated, permissions
from django.shortcuts import render
from rest_framework import viewsets
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from .filter import CommentFilter, PostFilter  # Add this import if CommentFilter is defined in filters.py
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from notifications.models import Notification
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from notifications.views import create_notification
# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = PostSerializer
    search_fields = ['content', 'author__username', 'created_at']
    

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = CommentFilter
    search_fields = ['content', 'author__username']

    def perform_create(self, serializer):
        comment = serializer.save(author=self.request.user)
        post = comment.post
        if post.author != self.request.user:
            create_notification(
                recipient=post.author,
                actor=self.request.user,
                verb="commented on your post",
                target=comment
            )

    def perform_update(self, serializer):
        comment = serializer.save()
        post = comment.post
        if post.author != self.request.user:
            create_notification(
                recipient=post.author,
                actor=self.request.user,
                verb="updated a comment on your post",
                target=comment
            )


class FeedView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # Get users that the current user is following
        following_users = self.request.user.following.all()
        # get posts from those users, ordered by created_date (most recent first)
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


from rest_framework import generics

class LikePostView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if not created:
            return Response({"message": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)
        # Notification using Notification.objects.create
        if post.author != request.user:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked your post",
                content_type=ContentType.objects.get_for_model(Post),
                object_id=post.id,
                target=post
            )
        return Response({"message": "Post liked successfully!"}, status=status.HTTP_200_OK)

class UnlikePostView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        like = Like.objects.filter(user=request.user, post=post).first()
        if not like:
            return Response({"message": "You have not liked this post."}, status=status.HTTP_400_BAD_REQUEST)
        like.delete()
        # Notification using Notification.objects.create
        if post.author != request.user:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="unliked your post",
                content_type=ContentType.objects.get_for_model(Post),
                object_id=post.id,
                target=post,
                is_read=True
            )
        return Response({"message": "Post unliked successfully!"}, status=status.HTTP_200_OK)

    
