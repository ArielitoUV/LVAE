from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class UsuarioAdmin(UserAdmin):
    list_display = ('email', 'nombre', 'apellido', 'user_type', 'is_active')
    list_filter = ('user_type', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Información personal', {'fields': ('nombre', 'apellido', 'fecha_nacimiento', 'telefono', 'estado', 'ciudad')}),
        ('Permisos', {'fields': ('is_active', 'is_staff')}),
        ('Tipo de usuario', {'fields': ('user_type',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nombre', 'apellido', 'fecha_nacimiento', 'telefono', 'estado', 'ciudad', 'password1', 'password2', 'user_type'),
        }),
    )
    ordering = ('email',)

    filter_horizontal = ()

admin.site.register(Usuario, UsuarioAdmin)