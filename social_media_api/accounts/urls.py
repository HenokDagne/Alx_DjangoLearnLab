from django.urls import path
from .views import RegisterView, LoginView, ProfileView, FollowUserView, UnfollowUserView


urlpatterns = [
	path('register/', RegisterView.as_view(), name='register'),
	path('login/', LoginView.as_view(), name='login'),
	path('profile/', ProfileView.as_view(), name='profile'),
    path('follow/<int:pk>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:pk>/', UnfollowUserView.as_view(), name='unfollow-user'),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user-alt'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user-alt'),
]
