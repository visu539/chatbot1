from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import AccountViewSet, HoldingViewSet, TransactionViewSet, SIPViewSet, client_aum

router = DefaultRouter()
router.register(r"accounts", AccountViewSet)
router.register(r"holdings", HoldingViewSet)
router.register(r"transactions", TransactionViewSet)
router.register(r"sips", SIPViewSet)

urlpatterns = [
    path("clients/<int:client_id>/aum/", client_aum, name="client-aum"),
]
urlpatterns += router.urls