# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from .models import Usuario
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label=_("Correo Electrónico"),
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su correo electrónico', 'autofocus': False}),
    )

    nombre = forms.CharField(
        label=_("Nombre"),
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su nombre'}),
    )

    apellido = forms.CharField(
        label=_("Apellido"),
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su apellido'}),
    )

    telefono = forms.CharField(
        label=_("Teléfono"),
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su número de teléfono'}),
    )

    estado = forms.CharField(
        label=_("Estado"),
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el Estado donde vive'}),
    )

    ciudad = forms.CharField(
        label=_("Ciudad"),
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su Ciudad'}),
    )

    user_type = forms.ChoiceField(
    label=_("Tipo de Usuario"),
    choices=[('', 'Seleccione una opción'), ('apoderado', 'Apoderado'), ('alumno', 'Alumno')],
    widget=forms.Select(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = Usuario
        fields = ['user_type', 'nombre', 'apellido', 'telefono', 'estado', 'ciudad', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error_messages['password_mismatch'] = _("Las contraseñas no coinciden.")
        self.error_messages['password_too_short'] = _("La contraseña debe tener al menos 8 caracteres.")
        self.error_messages['password_common'] = _("La contraseña no puede ser una contraseña común.")
        self.error_messages['password_entirely_numeric'] = _("La contraseña no puede ser completamente numérica.")
        self.error_messages['email_in_use'] = _('Este email ya está en uso. Por favor, elige otro.')
        self.fields['user_type'].widget.attrs['readonly'] = True