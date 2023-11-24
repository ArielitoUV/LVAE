"""LVAE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from core import views
from core.views import registrar_usuario

urlpatterns = [
    path('',views.index,name="index"),
    path('iniciosesion/',views.iniciosesion,name="iniciosesion"),
    path('iniciosesion_en/',views.iniciosesion,name="iniciosesion"),
    path('registroap/', registrar_usuario, name='registrar_usuario'),
    path('rs/',views.rs,name="rs"),
    path('gestionperfil/',views.gestionperfil,name="gestionperfil"),
    path('donaciones/',views.donaciones,name="donaciones"),
    path('becas/',views.becas,name="becas"),
    path('admin/', admin.site.urls),

]
