from django.urls import path
from . import views

app_name = "contacto"
urlpatterns = [
    path("", views.contact, name="contact_page"),
    # path("/send", views.send_message, name="send_message")
]
