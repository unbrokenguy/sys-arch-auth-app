"""Auth app urls.
POST /api/auth/sign_in/ - Sign In view.
POST /api/auth/sign_up/ - Sign Up view.
Get /api/user/ - Retrieve authenticated User.
"""
from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("auth_api.urls", namespace="api")),
]


