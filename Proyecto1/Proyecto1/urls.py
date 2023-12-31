"""
URL configuration for Proyecto1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from .views import saludo, despedida, dameFecha, calculaEdad, inicioBuscador, buscador
from .views import inicioBuscador, buscador
from django.views.generic import RedirectView

urlpatterns = [
    path('', inicioBuscador, name='inicioBuscador'),
    path('admin/', admin.site.urls),
    # path('saludo/', saludo, name='saludo'),
    # path('adios/', despedida, name='despedida'),
    # path('fecha/', dameFecha, name='dameFecha'),
    # path('edades/<int:edad>/<int:agno>', calculaEdad, name='calculaEdad'),
    path('inicio/', inicioBuscador, name='inicioBuscador'),
    path('buscar/<str:buscar>/', buscador, name='buscador'),
]
