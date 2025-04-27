from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import(
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/v1/docs/', SpectacularSwaggerView.as_view(), name='swagger_ui'),
    path('api/v1/redoc/', SpectacularRedocView.as_view(), name='redoc'),
    path('api/v1/', include('accounts.urls')),
    path('api/v1/', include('authentication.urls')),
    path('api/v1/', include('administrators.urls')),
    path('api/v1/', include('collects.urls')),
    path('api/v1/', include('customers.urls')),
    path('api/v1/', include('orders.urls')),
    path('api/v1/', include('products.urls')),
    path('admin/', admin.site.urls),
]