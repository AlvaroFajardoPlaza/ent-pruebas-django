from django.urls import path
#from .views import index
from . import views

app_name="gestion"
urlpatterns = [
    path("", views.index),
    path("/<int:product_id>", views.show_details, name="show_details")
]