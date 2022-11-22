from django import forms
from .models import Producto, Prestamo, Usuario


class PrestamoFormulario(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = [  'idProducto']