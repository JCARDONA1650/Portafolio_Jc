from django.urls import path
from . import views

urlpatterns = [
    # URL DE HOME
    path('', views.indexview, name='index'),

    # URL DE REGISTRO
    path('registro/', views.registro_view, name='registro'),
    # URL DE LOGIN
    path('login/', views.login_view, name='login'),
    # URL DE LOGOUT
    path('logout/', views.logout_view, name='logout'),


    # URL REGISTRO EXITOSO
    path('registro_exitoso/', views.registro_exitoso_view, name='registro_exitoso'),
    path('login_exitoso/', views.login_exitoso_view, name='login_exitoso'),


    # URL DE HOME USUARIO
    path('home-us/', views.home_usView, name='home_us'),


    # URL DE INFORMACION
    path('info/', views.infoview, name='info'),
    # URL DE CLIENTES
    path('clientes/', views.clientesviews, name='clientes'),
    # URL DE BLOG
    path("blog/", views.blogviews, name="blog"),
    # URL DE WORKSPACE
    path("workspace/", views.workiews, name="workspace"),
    # URL DE CONTACTO
    path("contacto/", views.contactoviews, name="contacto"),
    # URL DE FORMULARIOS
    path("formulario/", views.formularioviews, name="formulario")


]
