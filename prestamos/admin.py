from django.contrib import admin
from .models import Usuario, Producto, Prestamo


class ProductoAdmin(admin.ModelAdmin):
    list_display = ["idProducto","nombre" ]
    list_editable = ["nombre"]
    list_per_page = 5


class PrestamoAdmin(admin.ModelAdmin):
    list_display = ["idProducto","idUsuario", "estado", "fechaPrestamo", "fechaDevolucion" ]
    list_editable= ["estado"]

admin.site.register(Producto,ProductoAdmin)    
admin.site.register(Usuario)   
admin.site.register(Prestamo, PrestamoAdmin)   