from django.urls import path, include
from .views import SignUpView, ProfileView, ProfileUpdateView
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
]
