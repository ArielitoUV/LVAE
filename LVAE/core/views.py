# views.py
from django.shortcuts import render, redirect
from core.forms import CustomUserCreationForm

def registrar_usuario(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Puedes realizar alguna acción adicional después del registro exitoso
            return redirect('iniciosesion/')  
    else:
        form = CustomUserCreationForm()

    return render(request, 'core/registroap.html', {'form': form})

def index(request):
    return render(request, "core/index.html")

def iniciosesion(request):
    return render(request, "core/iniciosesion.html")






def rs(request):
    return render(request, "core/rs.html")

def gestionperfil(request):
    return render(request, "core/gestionperfil.html")

def donaciones(request):
    return render(request, "core/donaciones.html")

def becas(request):
    return render(request, "core/becas.html")


