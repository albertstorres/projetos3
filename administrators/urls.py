from django.urls import path, include
from rest_framework.routers import DefaultRouter
from administrators.views import AdministratorViewSet

router = DefaultRouter()

router.register('administrators', AdministratorViewSet)

urlpatterns = [
    path('', include(router.urls))
]