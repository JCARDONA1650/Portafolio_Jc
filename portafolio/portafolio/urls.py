from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # URL DE administrador
    path('admin/', admin.site.urls),
    # URL INCLUDE URL DE LA APP
    path('', include('mi_portafolio.urls')),
]
