# urls.py
from django.contrib import admin
from django.urls import path

from auth_app.views import LoginView, ProtectedView, RegisterView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("protected/", ProtectedView.as_view(), name="protected"),
]
