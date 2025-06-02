from django.urls import path, include
from rest_framework.routers import DefaultRouter
from accounts.views import AccountViewSet, DepositViewSet, GetBalanceView

router = DefaultRouter()

router.register('account', AccountViewSet)
router.register('deposit', DepositViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('balance/', GetBalanceView.as_view(), name='get-balance'),
]