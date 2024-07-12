# urls.py
from django.contrib import admin
from django.urls import path

from auth_app.views import LoginView, ProtectedView, RegisterView
from mcqs.views import MCQListCreateView, MCQRetrieveUpdateDestroyView

urlpatterns = [
    path("mcqs/", MCQListCreateView.as_view(), name="mcq-list-create"),
    path("mcqs/<uuid:pk>/", MCQRetrieveUpdateDestroyView.as_view(), name="mcq-detail"),
]
