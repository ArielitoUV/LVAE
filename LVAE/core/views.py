from django.shortcuts import render, redirect
from core.forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .forms import UserProfileForm
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
            return redirect('index')
        else:
            print(form.errors)
    else:
        # Si no es una solicitud POST, crea un nuevo formulario (limpio)
        form = CustomAuthenticationForm()
    return render(request, 'core/iniciosesion.html', {'form': form})



@login_required
def gestion_perfil(request):
    usuario = request.user

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=usuario)
        password_form = PasswordChangeForm(user=usuario, data=request.POST)

        if form.is_valid() and password_form.is_valid():
            form.save()
            update_session_auth_hash(request, usuario)  
            password_form.save()
            messages.success(request, 'Tus datos se han actualizado correctamente.')
            return redirect('gestion_perfil')
    else:
        form = UserProfileForm(instance=usuario)
        password_form = PasswordChangeForm(user=usuario)

    context = {
        'form': form,
        'password_form': password_form,
    }

    return render(request, 'core/gestionperfil.html', context)


def index(request):
    return render(request, "core/index.html")


def rs(request):
    return render(request, "core/rs.html")


def gestionperfil(request):
    return render(request, "core/gestionperfil.html")

# from django.shortcuts import render, redirect
# from django.contrib import messages
# from .forms import PerfilForm


# @login_required
# def gestionperfil(request):
#     if request.method == 'POST':
#         form = PerfilForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Perfil actualizado exitosamente.')
#             return redirect('index')
#         else:
#             messages.error(request, 'Hubo un error al actualizar el perfil. Por favor, corrija los errores.')
#     else:
#         form = PerfilForm(instance=request.user)

#     return render(request, 'gestionperfil.html', {'form': form})


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