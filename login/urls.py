from django.urls import path, include
from login.views import UserRegistration,UserLoginView
urlpatterns = [
    path("register/",UserRegistration.as_view(),name="register"),
    path("login/",UserLoginView.as_view(),name="login")

    ]