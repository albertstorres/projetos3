from django.urls import path, include
from rest_framework.routers import DefaultRouter
from accounts.views import AccountViewSet, DepositViewSet

router = DefaultRouter()

router.register('account', AccountViewSet)
router.register('deposit', DepositViewSet)

urlpatterns = [
    path('', include(router.urls))
]