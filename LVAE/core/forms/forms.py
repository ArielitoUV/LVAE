from django import forms
from .models import Usuario

class RegistroUsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'telefono', 'estado', 'ciudad', 'email', 'password', 'user_type']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError('Este email ya está en uso. Por favor, elige otro.')
        return email
