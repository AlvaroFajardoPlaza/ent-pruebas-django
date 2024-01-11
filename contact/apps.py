from django.apps import AppConfig

class ContactConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "contact"

    # El verbose name nos permite cambiar el nombre que recibirá esta app en el panel de admin de Django.
    verbose_name="Mensajes de contacto"
