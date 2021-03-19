from rest_framework.routers import SimpleRouter

from auth_api.views import AuthViewSet, UserViewSet

app_name = "core"

router = SimpleRouter()
router.register("auth", AuthViewSet, basename="auth")
router.register("user", UserViewSet, basename="user")

urlpatterns = []

urlpatterns += router.urls
