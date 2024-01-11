from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    """Dentro de esta clase, si creamos nuestro formulario de contacto
    Pero para poder utilizar el método ModelForm, tendremos que crear una subclase 'META' con la clase que generamos en models.py
    """

    # Podemos darle estilos al formulario de esta manera o empleando Crispy Forms.
    name=forms.CharField(label="Nombre y Apellidos", max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control mt-2 mb-3', 'placeholder':'Introduzca sus datos'}))

    message= forms.CharField(label="Mensaje", max_length=500, required=True, widget=forms.Textarea(attrs={'class': 'form-control mt-2 mb-3', 'placeholder':'Expliquenos algunos de los detalles'}))

    class Meta:
        model = Contact

        # A continuación, los fields-campos- de nuestro formulario. Omitimos el field de 'created_at' porque ese se creará cuando se introduzcan las instancias en la BBDD
        # fields = '__all__' ////----> Esto nos crearía un campo por cada atributo de nuestro modelo, sin obviar el campo de 'created_at'
        fields = ['name', 'surname', 'email', 'contact_type', 'message', 'subscription']
        

