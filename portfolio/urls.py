"""
URL definitions for the portfolio application.

These routes map clean URL paths to view functions defined in
``portfolio.views``. Each path has a name so that it can be referenced
from templates when building navigation menus.
"""

from __future__ import annotations

from django.urls import path

from . import views


app_name = 'portfolio'

urlpatterns = [
    path('', views.home, name='home'),
    path('experiencia/', views.experience, name='experience'),
    path('educacion/', views.education, name='education'),
    path('habilidades/', views.skills, name='skills'),
    path('contacto/', views.contact, name='contact'),
]