from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, LeadViewSet

router = DefaultRouter()
router.register(r"clients", ClientViewSet, basename="client")
router.register(r"leads", LeadViewSet, basename="lead")

urlpatterns = router.urls