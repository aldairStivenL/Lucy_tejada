from django.db import models
from django.contrib.auth.models import AbstractUser

# Opciones para roles y género
ROLES = (
    ('admin', 'Administrador'),
    ('formador', 'Formador'),
    ('estudiante', 'Estudiante'),
)

GENERO = (
    ('M', 'Masculino'),
    ('F', 'Femenino'),
)

# Modelo personalizado de usuario
class User(AbstractUser):
    rol = models.CharField(max_length=10, choices=ROLES)
    telefono = models.CharField(max_length=15, blank=True)
    genero = models.CharField(max_length=1, choices=GENERO, blank=True)

    def __str__(self):
        return f"{self.username} ({self.get_rol_display()})"

# Modelo para los cursos
class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    cupo_maximo = models.IntegerField()
    formador = models.ForeignKey(User, limit_choices_to={'rol': 'formador'}, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nombre

# Modelo para las inscripciones
class Inscripcion(models.Model):
    estudiante = models.ForeignKey(User, limit_choices_to={'rol': 'estudiante'}, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    asistencia = models.JSONField(default=list)  # Lista de fechas de asistencia
    calificacion = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.estudiante.username} en {self.curso.nombre}"