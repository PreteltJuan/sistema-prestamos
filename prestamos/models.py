
from django.db import models

class Usuario(models.Model):
    
    idUsuario = models.CharField( primary_key=True, max_length=8)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

    def __str__(self):
        return str(self.idUsuario)


class Producto(models.Model):
    
    idProducto = models.AutoField(primary_key=True, null=False)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return str(self.nombre)


class Prestamo(models.Model):
    
    idPrestamo = models.AutoField(primary_key=True, null=False)
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    idUsuario =  models.ForeignKey(Usuario, on_delete=models.CASCADE)
    estado = models.BooleanField(default=False)
    fechaPrestamo = models.DateTimeField(auto_now_add=True)
    fechaDevolucion = models.DateTimeField(auto_now = True)
 
