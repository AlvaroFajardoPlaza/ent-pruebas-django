from django.shortcuts import get_object_or_404, render

#Django Paginator nos permite paginar los resultados y también nos permite acceder a las excepciones de uso
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage

# Importamos el módulo http y sus errores...
from django.http import HttpResponse, Http404, HttpResponseNotFound

from .models import Product

# Create your views here.
def index(req=None):
    # Esto nos imprime por consola los productos que hayamos guardado antes... Podemos guardarlo en una variable... etc
    # print(Product.objects.all())
    products = Product.objects.all()
    products_page = Paginator(products, 2) # Muestra dos productos de la lista

    page_number = req.GET.get('page')

    # products_list = products_page.get_page(page_number) #### método get_page
    #### Con el método .page() podemos manejar los errores sobre el paginador
    try:
        products_list = products_page.page(page_number)
    except EmptyPage:
        products_list = products_page.page('1')
        print("Página vacia. Te mandamos a la página 1...")
    except PageNotAnInteger:
        products_list = products_page.page('1')
        print("No has introducido ningún número válido para el paginador. Te mandamos a la página 1...")
    except InvalidPage:
        products_list = products_page.page('1')
        print("Página no válida. Te mandamos a la página 1...")
    except Exception as e:
        print(type(e).__name__, e)
        print("Error genérico")

    # El tercer parámetro diccionario -opcional- es el que pasamos para poder ser consultado desde la plantilla html
    return render(req, "index.html", {
        'products': products_list,
        }) # Este es el nombre con el que nos referiremos a los productos en el HTML para hacer for, if... etc



# GENERAMOS LA FUNCIÓN QUE NOS DEVUELVE LOS DETALLES DE UN SOLO PRODUCTO
def show_details(req, product_id):
    # Método sencillo.
    product = get_object_or_404(Product, id=product_id)

    # Realizamos el manejo de errores con try / except ---> Método complejo
    """try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return HttpResponseNotFound()
    except Exception as e:
        print("Error genérico", e, type(e).__name__)
    """
    return render(req, "show_details.html", {
        'product': product
        })


