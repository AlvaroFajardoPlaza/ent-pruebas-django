from django.db import models

# Aquí creamos esos motivos de contacto para nuestros futuros mensajes
contact_options = [
    [0, "Pedido de información"],
    [1, "Reclamaciones de productos"],
    [2, "Felicitaciones"],
]

class Contact(models.Model):
    """Esta clase contiene la información de las personas y los mensajes cuando contactan a través de un form.

    - name: nombre del usuario. Required.
    - surname: apellidos.
    - email: el mail del usuario o persona que contacta. Required
    - message: tipo texto y requerido
    - contact_type: lista de las posibles opcion del "por qué" contacta con nosotros este usuario/persona
    - subscription: Si la persona o el usuario desea subscribirse al boletín de not¡cias
    - created_at: es un campo de tipo DateField para señalar cuando se crea esta instancia o mensaje de contacto
    """
    
    name = models.CharField(max_length=30, verbose_name="Nombre")
    surname = models.CharField(max_length=50, verbose_name="Apellidos")
    email = models.EmailField(verbose_name="Correo Electrónico")
    contact_type = models.IntegerField(choices=contact_options, verbose_name="Motivo de contacto")
    message = models.CharField(max_length=255, verbose_name="Mensaje")
    subscription = models.BooleanField(default=False, verbose_name="Subscripción a la Newsletter")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de envío")

    def __str__(self):
        return "{} {}. Email: {}. Message: {}".format(self.name, self.surname, self.email, self.message)
