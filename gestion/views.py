from django.shortcuts import render

from .models import Product

# Create your views here.
def index(req=None):
    # Esto nos imprime por consola los productos que hayamos guardado antes... Podemos guardarlo en una variable... etc
    # print(Product.objects.all())
    products = Product.objects.all()

    for p in products:
        print(p)

    # El tercer parámetro diccionario -opcional- es el que pasamos para poder ser consultado desde la plantilla html
    return render(req, "index.html", {
        'products': products,
        }) # Este es el nombre con el que nos referiremos a los productos en el HTML para hacer for, if... etc

