from django.shortcuts import render, redirect
from core.forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import authenticate, login

def registrar_usuario(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
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
        # Si no es una solicitud POST, crea un nuevo formulario (limpio)
        form = CustomAuthenticationForm()

    return render(request, 'core/iniciosesion.html', {'form': form})


def index(request):
    return render(request, "core/index.html")


def rs(request):
    return render(request, "core/rs.html")


def gestionperfil(request):
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