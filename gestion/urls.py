from django.urls import path
#from .views import index
from . import views

app_name="gestion"
urlpatterns = [
    path("", views.index, name="index"),
    path("/<int:product_id>", views.show_details, name="show_details"),
    path("/create_product", views.create_product, name="create_product"),
    path("/update_product/<int:product_id>", views.update_product, name="update_product"),
    path("/delete/<int:product_id>", views.delete, name="delete")

]