from django.urls import path, include
from .views import SignUpView, ProfileView, ProfileUpdateView, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CommentUpdateView, CommentDeleteView, CommentCreateView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("register/", SignUpView.as_view(), name="templates/registration/signup"),
    path(
        "profile/",
        ProfileView.as_view(),
        name="profile",
    ),
    path(
        "login/",
        LoginView.as_view(template_name="registration/login.html", next_page="profile"),
        name="login",
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/update", ProfileUpdateView.as_view(), name="profile_update")
    ,
    # CRUD URLs for Post
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:post_pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('posts/<int:post_pk>/comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment-update'),
    path('posts/<int:post_pk>/comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
