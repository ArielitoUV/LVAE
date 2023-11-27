from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate
from .models import Usuario
from django import forms



class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label=_('Correo electrónico'),
        widget=forms.EmailInput(attrs={'autofocus': False,'class':'form-control', 'placeholder': 'Ingrese corrreo electronico'}),
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
        fields = ['email', 'nombre', 'apellido', 'telefono', 'estado', 'ciudad','user_type', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error_messages['password_mismatch'] = _("Las contraseñas no coinciden.")
        self.error_messages['password_too_short'] = _("La contraseña debe tener al menos 8 caracteres.")
        self.error_messages['password_common'] = _("La contraseña no puede ser una contraseña común.")
        self.error_messages['password_entirely_numeric'] = _("La contraseña no puede ser completamente numérica.")
        self.error_messages['email_in_use'] = _('Este email ya está en uso. Por favor, elige otro.')
        self.fields['user_type'].widget.attrs['readonly'] = True


class CustomAuthenticationForm(AuthenticationForm):
    email = forms.EmailField(label=_('Correo electrónico'), widget=forms.EmailInput(attrs={'autofocus': False}))
    password = forms.CharField(label=_('Contraseña'), strip=False, widget=forms.PasswordInput)

    error_messages = {
        'invalid_login': _(
            "Por favor, ingrese un %(username)s válido y contraseña"
        ),
        'inactive': _("Esta cuenta está inactiva."),
    }


