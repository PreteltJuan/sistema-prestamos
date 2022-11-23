from django.urls import path
from . import views



urlpatterns = [
    path("home", views.home,  name="home"),
    path("hacerPrestamo", views.hacerPrestamo, name="hacerPrestamo"),
    path("obtenerPrestamos", views.obtenerPrestamos, name="obtenerPrestamos"),
    path("obtenerUsuario/<id>", views.obtenerUsuario, name="obtenerUsuario"),
    path("hacerDevolucion/<id>", views.hacerDevolucion, name="hacerDevolucion")
]   

