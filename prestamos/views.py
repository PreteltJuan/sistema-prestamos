
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import PrestamoFormulario
from .models import Prestamo, Usuario
from datetime import date
from django.http import JsonResponse

prestamos_user = None

def home(request):
    form1 = PrestamoFormulario()
    prestamos = Prestamo.objects.all()
    return render(request, 'pages/home.html', { 'form1' : form1, 'prestamos':prestamos})

def hacerPrestamo(request):
    text = request.POST.get('leerUsuario-label1', '')
    try:
        usuario = Usuario.objects.get(idUsuario = text)
    except:
        form1 = PrestamoFormulario()
        prestamos = Prestamo.objects.all()
        return render(request, 'pages/home.html', { 'form1' : form1, 'prestamos':prestamos, 'error':1})
    print(text)
    if request.method == 'POST':
        form = PrestamoFormulario(request.POST)
        if form.is_valid():
            
            prestamo = form.save(commit=False)
            prestamo.idUsuario = usuario
            prestamo.save()
    return redirect('home')

def obtenerPrestamos(request):
    text = request.POST.get('leerUsuario-label2', '')
    try:
        usuario = Usuario.objects.get(idUsuario = text )
    except:
        form1 = PrestamoFormulario()
        prestamos = Prestamo.objects.all()
        return render(request, 'pages/home.html', { 'form1' : form1, 'prestamos':prestamos, 'error':1})
    request.session['user-prestamos'] = text
    prestamos_user = Prestamo.objects.filter(  estado = False, idUsuario = usuario )
    form1 = PrestamoFormulario()
    prestamos = Prestamo.objects.all()
    return render(request, 'pages/home.html', { 'form1' : form1, 'prestamos':prestamos, 'prestamos_user':prestamos_user})


    request.session["idUsuario"] = id
    #return HttpResponse('SD5A23D8')
    

def obtenerUsuario(request, id):
    try:
        usuario = Usuario.objects.get(idUsuario = id)
        return HttpResponse((usuario.nombre + " " +usuario.apellido))
    except:
        return HttpResponse("USUARIO NO ECONTRADO")
        
def hacerDevolucion(request, id):
    prestamo = Prestamo.objects.get(idPrestamo = id)
    prestamo.estado = True
    prestamo.save()
    prestamos = Prestamo.objects.all()
    form1 = PrestamoFormulario()
    text = request.session['user-prestamos']
    usuario = Usuario.objects.get(idUsuario = text )
    prestamos_user = Prestamo.objects.filter(  estado = False, idUsuario = usuario )
    return render(request, 'pages/home.html', { 'form1' : form1, 'prestamos':prestamos, 'prestamos_user':prestamos_user})
