from django.shortcuts import get_object_or_404, render, redirect

#Django Paginator nos permite paginar los resultados y también nos permite acceder a las excepciones de uso
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage

# Importamos el módulo http y sus errores...
from django.http import HttpResponse, Http404, HttpResponseNotFound

from .models import Product
from .forms import ProductForm

# Create your views here.
def index(req=None):
    # Esto nos imprime por consola los productos que hayamos guardado antes... Podemos guardarlo en una variable... etc
    # print(Product.objects.all())
    products = Product.objects.all()
    products_page = Paginator(products, 3) # Muestra dos productos de la lista

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

# FUNCIÓN QUE NOS SIRVE PARA CREAR UN NUEVO PRODUCTO
def create_product(req):
    form = ProductForm()

    if req.method == "POST": # Aquí planteamos la primera validación, chequeando si el formulario es de tipo POST
        print(req.POST)
        form = ProductForm(req.POST)

        # Finalizamos comprobando la validez de los datos enviados y creando el nuevo producto.
        if form.is_valid():
            # print(form)
            print("Formulario válido")

            new_product = Product()

            new_product.name = form.cleaned_data["name"]
            new_product.description = form.cleaned_data["description"]
            new_product.price = form.cleaned_data["price"]
            new_product.category = form.cleaned_data["category"]

            new_product.save()
            return redirect("gestion:index")

        else:
            print("El formulario no es válido")

    # Devolvemos la plantilla HTML de este formulario
    return render(req, "save_product.html", { "form": form })



# UPDATE DE UN PRODUCTO
def update_product(req, product_id):
    # 1º Buscamos el producto que tenemos que editar por su id
    product = get_object_or_404(Product, id=product_id)

    form = ProductForm(initial={'name': product.name,
                                'description': product.description,
                                'price': product.price,
                                'category': product.category,})

    # A partir de este punto todo se va a mantener de la misma manera que en el POST!
    if req.method == "POST": # Aquí planteamos la primera validación, chequeando si el formulario es de tipo POST
        print(req.POST)
        form = ProductForm(req.POST)

        # Finalizamos comprobando la validez de los datos enviados y creando el nuevo producto.
        if form.is_valid():
            # print(form)
            print("Formulario válido")

            ##### new_product = Product() #### ESTA LÍNEA TENEMOS QUE ELIMINARLA EN EL UPDATE, PARA QUE NO SE CREE UN NUEVO PRODUCTO Y SE EDITE EL ANTERIOR!!!!

            product.name = form.cleaned_data["name"]
            product.description = form.cleaned_data["description"]
            product.price = form.cleaned_data["price"]
            product.category = form.cleaned_data["category"]

            product.save()
            return redirect("gestion:index")

        else:
            print("El formulario no es válido")

    # Devolvemos la plantilla HTML de este formulario
    return render(req, "save_product.html", { "form": form })


# DELETE PRODUCT --->
def delete(req, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect("gestion:index")