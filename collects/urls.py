from django.urls import path, include
from rest_framework.routers import DefaultRouter
from collects.views import AddressViewSet, CategorieViewSet, CollectViewSet

router = DefaultRouter()

router.register('address', AddressViewSet)
router.register('categories', CategorieViewSet)
router.register('collects', CollectViewSet)

urlpatterns = [
    path('', include(router.urls))
]