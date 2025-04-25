#from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/v1/', include('authentication.urls')),
    path('api/v1/', include('administrators.urls')),
    path('api/v1/', include('collects.urls')),
    #path('api/v1/', include('customers.urls')),
    path('api/v1/', include('products.urls')),
    #path('admin/', admin.site.urls),
]