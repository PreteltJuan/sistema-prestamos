from django.shortcuts import render, redirect
from .forms import PrestamoFormulario
from .models import Prestamo
from datetime import date

def home(request):
   form1 = PrestamoFormulario()
   prestamos = Prestamo.objects.all()
   return render(request, 'pages/home.html', { 'form1' : form1, 'prestamos':prestamos})

def hacerPrestamo(request):
    
    if request.method == 'POST':
        form = PrestamoFormulario(request.POST)
        if form.is_valid():
            prestamo = form.save()
    return redirect('home')