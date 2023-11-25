from django.contrib import admin
from django.urls import path
from core import views
from core.views import registrar_usuario,iniciar_sesion

urlpatterns = [
    path('',views.index,name="index"),
    path('iniciosesion/', iniciar_sesion, name='iniciar_sesion'),
    path('registroap/', registrar_usuario, name='registrar_usuario'),
    path('rs/',views.rs,name="rs"),
    path('gestionperfil/',views.gestionperfil,name="gestionperfil"),
    path('donaciones/',views.donaciones,name="donaciones"),
    path('becas/',views.becas,name="becas"),
    path('admin/', admin.site.urls),
]
