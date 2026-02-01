from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    ESTADOS =(
        ('pendiente', 'Pendiente'),
        ('aprobado', 'Aprobado'),
        ('rechazado', 'Rechazado'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    es_alumno = models.BooleanField(default=False)
    es_admin = models.BooleanField(default=False)

    estado=models.CharField(
        max_length=10,
        choices=ESTADOS,
        default='pendiente'
    )

    def __str__(self):
        return self.user.username