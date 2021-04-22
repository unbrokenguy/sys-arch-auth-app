"""Auth app urls.
POST /api/auth/sign_in/ - Sign In view.
POST /api/auth/sign_up/ - Sign Up view.
Get /api/user/ - Retrieve authenticated User.
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("auth_api.urls", namespace="api")),
]
