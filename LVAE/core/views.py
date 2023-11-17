from django.shortcuts import render

def index(request):
    return render(request, "core/index.html")

def iniciosesion(request):
    return render(request, "core/iniciosesion.html")

def registroap(request):
    return render(request, "core/registroap.html")

def rs(request):
    return render(request, "core/rs.html")

def gestionperfil(request):
    return render(request, "core/gestionperfil.html")

def donaciones(request):
    return render(request, "core/donaciones.html")

def comunidad(request):
    return render(request, "core/comunidad.html")

def becas(request):
    return render(request, "core/becas.html")
