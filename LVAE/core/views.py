from django.shortcuts import render, redirect
from core.forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import EditarPerfilForm, CambiarContraseñaForm
from django.contrib.auth import update_session_auth_hash


def registrar_usuario(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            # Renderizar la plantilla con los datos del usuario
            email_body = render_to_string('core/reporte_registro.txt', {'usuario': usuario})
            # Configurar el correo
            subject = 'Nuevo Registro de Usuario en La Via al Éxito'
            from_email = settings.EMAIL_HOST_USER
            to_email = ['reporteviaexito@gmail.com']
            # Configurar el correo como mensaje de texto plano
            message = EmailMessage(subject, email_body, from_email, to_email)
            message.send(fail_silently=False)
            # Redirige a la página de inicio de sesión después del registro exitoso
            return redirect('iniciar_sesion')
    else:
        # Si no es una solicitud POST, crea un nuevo formulario (limpio)
        form = CustomUserCreationForm()
    return render(request, 'core/registroap.html', {'form': form})
def iniciar_sesion(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Redirige a la página de inicio después del inicio de sesión exitoso
            return redirect('index2')
        else:
            print(form.errors)
    else:
        # Si no es una solicitud POST, crea un nuevo formulario (limpio)
        form = CustomAuthenticationForm()
    return render(request, 'core/iniciosesion.html', {'form': form})



from django.shortcuts import render, redirect
from .forms import EditarPerfilForm, CambiarContraseñaForm
from django.contrib import messages

def gestion_perfil(request):
    if not request.user.is_authenticated:
        return redirect('iniciar_sesion')
    
    editar_form = EditarPerfilForm(initial={
        'nombre': request.user.nombre,
        'apellido': request.user.apellido,
        'telefono': request.user.telefono,
        'fecha_nacimiento': request.user.fecha_nacimiento,
        'estado': request.user.estado,
        'ciudad': request.user.ciudad,
    })
    cambiar_password_form = CambiarContraseñaForm(user=request.user)
    
    if request.method == 'POST':
        editar_form = EditarPerfilForm(request.POST)
        cambiar_password_form = CambiarContraseñaForm(request.user, request.POST)
        
        if editar_form.is_valid():
            request.user.nombre = editar_form.cleaned_data['nombre']
            request.user.apellido = editar_form.cleaned_data['apellido']
            request.user.telefono = editar_form.cleaned_data['telefono']
            request.user.fecha_nacimiento = editar_form.cleaned_data['fecha_nacimiento']
            request.user.estado = editar_form.cleaned_data['estado']
            request.user.ciudad = editar_form.cleaned_data['ciudad']
            request.user.save()
            messages.success(request, 'Perfil actualizado exitosamente.')
            return redirect('gestion_perfil')
        
        if cambiar_password_form.is_valid():
            cambiar_password_form.save()
            update_session_auth_hash(request, cambiar_password_form.user)
            messages.success(request, 'Contraseña cambiada exitosamente.')
            return redirect('gestion_perfil')
    
    context = {
        'editar_form': editar_form,
        'cambiar_password_form': cambiar_password_form,
    }
    
    return render(request, 'gestionperfil.html', context)




def index(request):
    return render(request, "core/index.html")
def rs(request):
    return render(request, "core/rs.html")
def gestion_perfil(request):
    return render(request, "core/gestionperfil.html")
def donaciones(request):
    return render(request, "core/donaciones.html")
def pasoapaso(request):
    return render(request, "core/pasoapaso.html")
def acercade(request):
    return render(request, "core/acercade.html")
def unicolla(request):
    return render(request, "core/unicolla.html")
def secundaria(request):
    return render(request, "core/secundaria.html")
def index2(request):
    return render(request, "core/index2.html")
def infobecas(request):
    return render(request, "core/infobecas.html")