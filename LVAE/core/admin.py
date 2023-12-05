# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class UsuarioAdmin(UserAdmin):
    list_display = ('email', 'nombre', 'apellido', 'user_type', 'is_active', 'is_staff')
    search_fields = ('email', 'nombre', 'apellido')
    list_filter = ('user_type', 'is_active', 'is_staff')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Información personal', {'fields': ('nombre', 'apellido', 'fecha_nacimiento', 'telefono', 'estado', 'ciudad')}),
        ('Permisos', {'fields': ('user_type', 'is_active', 'is_staff')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nombre', 'apellido', 'user_type', 'password1', 'password2'),
        }),
    )

    ordering = ('email',)

# Registra el modelo Usuario en la interfaz de administrador
admin.site.register(Usuario, UsuarioAdmin)
