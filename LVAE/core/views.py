from django.shortcuts import render, redirect
from core.forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from core.forms import CustomAuthenticationForm
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
            # Autenticar al usuario
            user = authenticate(request, username=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user is not None:
                # Iniciar sesión
                login(request, user)
                # Redirigir a la página deseada después de iniciar sesión
                return redirect('registrar_usuario')
    else:
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

def becas(request):
    return render(request, "core/becas.html")


