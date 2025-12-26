from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    es_alumno = models.BooleanField(default=False)
    es_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username