from django.shortcuts import render, redirect
from core.forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import EditarPerfilForm, CambiarContraseñaForm


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



@login_required
def gestionar_perfil(request):
    if request.method == 'POST':
        perfil_form = EditarPerfilForm(request.POST)
        contraseña_form = CambiarContraseñaForm(user=request.user, data=request.POST)
        if perfil_form.is_valid():
            # Guardar cambios en el perfil del usuario
            request.user.nombre = perfil_form.cleaned_data['nombre']
            request.user.apellido = perfil_form.cleaned_data['apellido']
            request.user.telefono = perfil_form.cleaned_data['telefono']
            request.user.fecha_nacimiento = perfil_form.cleaned_data['fecha_nacimiento']
            request.user.estado = perfil_form.cleaned_data['estado']
            request.user.ciudad = perfil_form.cleaned_data['ciudad']
            request.user.save()
            messages.success(request, 'Los cambios en el perfil se han guardado correctamente.')

        if contraseña_form.is_valid():
            contraseña_form.save()
            messages.success(request, 'Tu contraseña ha sido cambiada exitosamente.')

        return redirect('gestionar_perfil')
    else:
        perfil_form = EditarPerfilForm(initial={
            'nombre': request.user.nombre,
            'apellido': request.user.apellido,
            'telefono': request.user.telefono,
            'fecha_nacimiento': request.user.fecha_nacimiento,
            'estado': request.user.estado,
            'ciudad': request.user.ciudad,
        })
        contraseña_form = CambiarContraseñaForm(user=request.user)

    context = {
        'perfil_form': perfil_form,
        'contraseña_form': contraseña_form,
    }
    return render(request, 'gestionar_perfil.html', context)




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