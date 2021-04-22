"""Auth Api urls.
POST /auth/sign_in/ - Sign In view.
POST /auth/sign_up/ - Sign Up view.
Get /user/ - Retrieve authenticated User.
"""
from rest_framework.routers import SimpleRouter

from auth_api.views import AuthViewSet, UserViewSet

app_name = "core"

router = SimpleRouter()
router.register("auth", AuthViewSet, basename="auth")
router.register("user", UserViewSet, basename="user")

urlpatterns = []

urlpatterns += router.urls
