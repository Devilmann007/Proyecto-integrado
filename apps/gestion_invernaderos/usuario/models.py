# ===============================
# MODELO: usuarios/models.py
# ===============================
from django.db import models  # Importamos el módulo que nos permite definir modelos/tablas
# Creamos la clase Usuario que hereda de models.Model (base para tablas de Django)
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)  # ID único autoincremental
    nombre = models.CharField(max_length=100)        # Nombre del usuario
    correo = models.EmailField(unique=True)          # Correo único
    contraseña = models.CharField(max_length=255)    # Contraseña (en texto plano por ahora)
    rol = models.CharField(max_length=50)            # Rol: agricultor o técnico
    fecha_registro = models.DateTimeField(auto_now_add=True)  # Fecha de creación automática

    # Método que define cómo se mostrará el objeto como texto
    def __str__(self):
        return self.nombre

