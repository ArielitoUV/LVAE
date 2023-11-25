# views.py
from django.shortcuts import render, redirect
from .forms import RegistroUsuarioForm

def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            # Puedes realizar alguna acción adicional después del registro exitoso
            return redirect('iniciosesion')  # Corregí el nombre de la URL
    else:
        form = RegistroUsuarioForm()

    return render(request, 'core/registroap.html', {'form': form})
