from django.db import models
from datetime import datetime
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

class TipoUsuario(models.Model):
    descripcion = models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.descripcion
    
class Comuna(models.Model):
    descripcion = models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.descripcion

class Region(models.Model):
    descripcion = models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.descripcion



class Cuenta(models.Model):
    correo = models.CharField(max_length=40)
    contraseña = models.CharField(max_length=10)
    fechaIngreso= models.DateField(default=datetime.now())
    def __str__(self) -> str:
        return self.correo

class Usuario(models.Model):
    rut = models.CharField(max_length=12)
    nombres = models.CharField(max_length=60)
    apellidos = models.CharField(max_length=60)
    fechaNacimiento = models.DateField()
    direccion = models.CharField(max_length=60)
    comuna = models.ForeignKey(Comuna,on_delete = models.CASCADE)
    region = models.ForeignKey(Region,on_delete = models.CASCADE)
    correo = models.ForeignKey(Cuenta,on_delete = models.CASCADE)
    tipoUsuario = models.ForeignKey(TipoUsuario,on_delete = models.CASCADE)
    telefono = models.CharField(max_length=14)
    def __str__(self) -> str:
        return self.rut


class TipoObra(models.Model):
    descripcion = models.CharField(max_length=40)
    def __str__(self) -> str:
        return self.descripcion


class SolicitudObra(models.Model):
    descripcion = models.CharField(max_length=40)
    def __str__(self) -> str:
        return self.descripcion











class Obra(models.Model):

    # SE VEN
    codigo = models.CharField(max_length=60,default="")
    nombre = models.CharField(max_length=60)
    precio = models.IntegerField()
    imagen =  models.ImageField(upload_to="media", blank=True, null=True)
    tipoObra = models.ForeignKey(TipoObra,on_delete = models.CASCADE)
    alto = models.IntegerField()
    largo = models.IntegerField()

    # NO SE VEN
    fechaIngreso= models.DateField(default=datetime.now())
    estadoSolicitud = models.ForeignKey(SolicitudObra,on_delete = models.CASCADE,default='PENDIENTE')
    NombreUsuario = models.CharField(max_length=60)
    def __str__(self) -> str:
        return self.codigo





class EstadoCompra(models.Model):
    estadoCompraDescripcion = models.CharField(max_length=60)
    def __str__(self) -> str:
        return self.estadoCompraDescripcion
    
class Compra(models.Model):
    Usuario = models.CharField(max_length=60)
    Obra = models.CharField(max_length=60,default="")
    estadoCompra = models.CharField(max_length=60,default="Carrito")
    def __str__(self) -> str:
        return self.Usuario






class Autentificacion(models.Model):
    NombreCliente = models.CharField(max_length=60)
    Correo = models.CharField(max_length=60)
    Direccion = models.CharField(max_length=60)
    Telefono = models.CharField(max_length=60)
    imagenAutentificacion = CloudinaryField('imagen')
    def __str__(self):
        return self.NombreCliente

class TipoBanco(models.Model):
    NombreBanco = models.CharField(max_length=60)
    def __str__(self):
        return self.NombreBanco 

class TipoCuenta(models.Model):
    NombreCuenta = models.CharField(max_length=60)
    def __str__(self):
        return self.NombreCuenta 
    
class DatosCooperativos(models.Model):
    NombreCuentaCooperativo = models.CharField(max_length=60)
    NombreCliente = models.CharField(max_length=120)
    Correo = models.CharField(max_length=60)
    Direccion = models.CharField(max_length=60)
    Telefono = models.CharField(max_length=60)
    Banco = models.ForeignKey(TipoBanco,on_delete = models.CASCADE)
    TipoCuenta = models.ForeignKey(TipoCuenta,on_delete = models.CASCADE)
    NroCuenta = models.CharField(max_length=20)
    imagenCooperativo =  models.ImageField(upload_to="obra", blank=True, null=True)
    def __str__(self):
        return self.NombreCuentaCooperativo 





class HistorialCompras(models.Model):
    fechaCompra = models.DateField(default=datetime.now)
    Usuario = models.CharField(max_length=60)
    datos =  models.CharField(max_length=1000,default='')

    def __str__(self):
        return f'Compra de {self.Usuario} el {self.fechaCompra}'