from django.contrib import admin
from .models import Category, Product


# Aquí registramos las clases que serán accesibles desde el panel de administración de Django
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    fields = ('title',)

admin.site.register(Category, CategoryAdmin)


# Generando la clase Producto en el panel de administración de Django
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category", "description")
    # fields = ("id", "title", "price", "category", "description") # Si queremos que aparezcan todos, no es necesario escribir esta línea
