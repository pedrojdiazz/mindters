from django.db import models

# Create your models here.
class Productos(models.Model):
    precio = models.DecimalField(decimal_places=2, max_digits=15)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
