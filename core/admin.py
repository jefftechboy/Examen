from django.contrib import admin
from .models import *
from admin_confirm import AdminConfirmMixin
from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.forms import AuthenticationForm



class TipoUsuarioAdmin(AdminConfirmMixin, admin.ModelAdmin):
    confirm_change = True
    confirm_add = True
    confirmation_fields = ['descripcion']
class ComunaAdmin(AdminConfirmMixin, admin.ModelAdmin):
    confirm_change = True
    confirm_add = True
    confirmation_fields = ['descripcion']
class RegionAdmin(AdminConfirmMixin, admin.ModelAdmin):
    confirm_change = True
    confirm_add = True
    confirmation_fields = ['descripcion']
class CuentaAdmin(AdminConfirmMixin, admin.ModelAdmin):
    confirm_change = True
    confirm_add = True
    confirmation_fields = ['correo', 'contraseña','fechaIngreso']
class UsuarioAdmin(AdminConfirmMixin, admin.ModelAdmin):
    confirm_change = True
    confirm_add = True
    confirmation_fields = ['rut', 
        'nombres','apellidos','fechaNacimiento','direccion','comuna','region'
        ,'correo','tipoUsuario','telefono']
class TipoObraAdmin(AdminConfirmMixin, admin.ModelAdmin):
    confirm_change = True
    confirm_add = True
    confirmation_fields = ['descripcion']
class SolicitudObraAdmin(AdminConfirmMixin, admin.ModelAdmin):
    confirm_change = True
    confirm_add = True
    confirmation_fields = ['descripcion']
class ObraAdmin(AdminConfirmMixin, admin.ModelAdmin):
    confirm_change = True
    confirm_add = True
    confirmation_fields = ['codigo', 'nombre','precio','imagen','tipoObra','alto',
        'largo','fechaIngreso','estadoSolicitud','NombreUsuario']
class CompraAdmin(AdminConfirmMixin, admin.ModelAdmin):
    confirm_change = True
    confirm_add = True
    confirmation_fields = ['Usuario', 'Obra','Cantidad','fechaCompra','PrecioFinal']
class AutentificacionAdmin(AdminConfirmMixin, admin.ModelAdmin):
    confirm_change = True
    confirm_add = True
    confirmation_fields = ['NombreCliente', 'Correo','Direccion','Telefono','imagenAutentificacion']
class TipoBancoAdmin(AdminConfirmMixin, admin.ModelAdmin):
    confirm_change = True
    confirm_add = True
    confirmation_fields = ['NombreBanco']
class TipoCuentaAdmin(AdminConfirmMixin, admin.ModelAdmin):
    confirm_change = True
    confirm_add = True
    confirmation_fields = ['NombreCuenta']
class DatosCooperativosAdmin(AdminConfirmMixin, admin.ModelAdmin):
    confirm_change = True
    confirm_add = True
    confirmation_fields = ['NombreCuentaCooperativo','NombreCliente','Correo','Direccion','Telefono'
        ,'Banco','TipoCuenta','NroCuenta','imagenCooperativo']
class HistorialCompraAdmin(AdminConfirmMixin, admin.ModelAdmin):
    confirm_change = True
    confirm_add = True
    confirmation_fields = ['NombreUsuario','Comprobantes']


# Register your models here.
admin.site.register(TipoUsuario,TipoUsuarioAdmin)
admin.site.register(Comuna,ComunaAdmin)
admin.site.register(Region,RegionAdmin)
admin.site.register(Cuenta,CuentaAdmin)
admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(TipoObra,TipoObraAdmin)
admin.site.register(SolicitudObra,SolicitudObraAdmin)
admin.site.register(Obra,ObraAdmin)
admin.site.register(Compra,CompraAdmin)
admin.site.register(Autentificacion,AutentificacionAdmin)
admin.site.register(TipoBanco,TipoBancoAdmin)
admin.site.register(TipoCuenta,TipoCuentaAdmin)
admin.site.register(DatosCooperativos,DatosCooperativosAdmin)
admin.site.register(HistorialCompras)