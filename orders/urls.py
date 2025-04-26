from django.urls import path, include
from rest_framework.routers import DefaultRouter
from orders.views import OrderViewSet, OrderProductsViewSet

router = DefaultRouter()

router.register('orders', OrderViewSet)
router.register('orders/products', OrderProductsViewSet)

urlpatterns = [
    path('', include(router.urls))
]