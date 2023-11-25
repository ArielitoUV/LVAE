from django.shortcuts import render, redirect
from core.forms import CustomUserCreationForm

def registrar_usuario(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirige a la página de inicio de sesión después del registro exitoso
            return redirect('iniciosesion')  
    else:
        # Si no es una solicitud POST, crea un nuevo formulario (limpio)
        form = CustomUserCreationForm()

    return render(request, 'core/registroap.html', {'form': form})

def index(request):
    return render(request, "core/index.html")

def iniciosesion(request):
    # Limpia los campos del formulario
    form = CustomUserCreationForm()
    
    return render(request, "core/iniciosesion.html", {'form': form})






def rs(request):
    return render(request, "core/rs.html")

def gestionperfil(request):
    return render(request, "core/gestionperfil.html")

def donaciones(request):
    return render(request, "core/donaciones.html")

def becas(request):
    return render(request, "core/becas.html")


