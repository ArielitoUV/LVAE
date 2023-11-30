# models.py
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, user_type=None, **extra_fields):
        if not email:
            raise ValueError('El email debe ser ingresado.')
        email = self.normalize_email(email)
        user = self.model(email=email, user_type=user_type, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, user_type=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, user_type, **extra_fields)

class Usuario(AbstractBaseUser):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    estado = models.CharField(max_length=100, blank=True, null=True)
    ciudad = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True)
    user_type = models.CharField(max_length=10, choices=[
        ('apoderado', 'Apoderado'),
        ('alumno', 'Alumno'),
    ])

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'apellido', 'user_type']

    def __str__(self):
        return self.email
