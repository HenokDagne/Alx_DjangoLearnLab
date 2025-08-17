from django.urls import path
from .views import SignUpView, ProfileView, ProfileUpdateView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("register/", SignUpView.as_view(), name="register"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("login/", LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("profile/update/", ProfileUpdateView.as_view(), name="profile_update"),
]