from rest_framework.routers import DefaultRouter
from .views import TrabalhoViewSet

app_name = "trabalho"

router = DefaultRouter()
router.register(r"", TrabalhoViewSet, basename="trabalho")

urlpatterns = router.urls