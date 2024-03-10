from django.db import models

# Create your models here.
from django.conf import settings

class Profile(models.Model):
    usuario          = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    fecha_nacimiento = models.DateField(blank = True, null = True)
    foto             = models.ImageField(upload_to = 'users/%Y/%m/%d/', blank = True)
    
    def __str__(self):
        return f'Perfil de {self.usuario.username}'