"""
URL configuration for the portfolio project.

Routes incoming HTTP requests to the appropriate views. This configuration
includes a path for the Django admin and delegates application‑specific
routes to the ``portfolio`` app. Feel free to extend this file with
additional URL patterns if you add new apps or endpoints.
"""

from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls', namespace='portfolio')),
]