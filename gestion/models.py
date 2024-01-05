from django.db import models

# Create your models here.
class Category(models.Model):
    # Esta es la clase Category... Descripción

    # COLUMNAS DE NUESTRA TABLA category en SQL: ---> Django añade automaticamente el field de "id" como PrimaryKey not null <---
    title = models.CharField(max_length=255)

    # Constructor principal de clase y sus métodos
    # def __init__(self):
    #     pass

    # def __str__(self):
    #     return ""


class Product(models.Model):
    # Clase Producto: define un producto, con su descripción, precio y categoria.

    name = models.CharField(max_length=255)
    description = models.TextField() 
    price = models.DecimalField(decimal_places=2, max_digits=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    # Constructor de clase, atributos y métodos de clase
    # def __init__(self):
    #     pass

    def __str__(self):
        return "Nombre: {} -- Precio: {}".format(self.name, self.price)