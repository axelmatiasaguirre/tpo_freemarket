from django.views.generic import  TemplateView
from django.shortcuts import render

#cada función crea una vista que devuelve una plantilla .html a través de la funcion render
def index(request):
    return render(request, 'index.html')

def ventas(request):
    return render(request, 'vender.html')

def sucursales(request):
    return render(request, 'sucursales.html')

def contacto(request):
    return render(request, 'contacto.html')

def venta_productos(request):
    return render(request, 'vender_productos.html')
