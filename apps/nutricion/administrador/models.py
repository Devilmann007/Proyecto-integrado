from django.db import models

# Create your models here.
class usuario(models.Model):
    nombre = models.CharField()
    apellido = models.CharField()
    correo = models.EmailField()
    telefono = models.IntegerField()
   
    rol_cliente = "cliente"
    rol_administrador = "administrador"

    rol_choices = [
        (rol_cliente, "cliente"),
        (rol_administrador, "administrador"),
    ]

    rol = models.CharField(
        max_length=30,
        choices=rol_choices,
        default=rol_cliente,
    )
  
    def __str__(self):
        return self.nombre
    


