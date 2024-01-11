from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect

from .models import Contact
from .forms import ContactForm

def contact(request):
    # 1. Generamos el formularios con el que vamos a trabajar
    contact_form = ContactForm()

    # 2. Comprobamos que el formulario es de tipo POST
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)

        # 3. Validamos la info
        if contact_form.is_valid():
            print("El form es válido")
            contact_form.save()

            # Tengo que avisar que todo fue bien
            return redirect(reverse("contacto:contact_page") + '?ok')

        else:
            print("El form NO es válido")
            return redirect(reverse("contacto:contact_page") + '?error')

    return render(request, "contactForm.html", { 'form': contact_form })

# def send_message(request):
#     """
#      # 1. Generamos el formularios con el que vamos a trabajar
#     contact_form = ContactForm()

#     # 2. Comprobamos que el formulario es de tipo POST
#     if request.method == "POST":
#         print(request.POST)
#         contact_form = ContactForm(request.POST)

#         # 3. Validamos y guardamos en la bbdd los datos que se envían en el formulario
#         if contact_form.is_valid():
#             print("El formulario es válido")

#             new_message = Contact(
#                 name = contact_form.cleaned_data['name'],
#                 surname = contact_form.cleaned_data['surname'],
#                 email = contact_form.cleaned_data['email'],
#                 message = contact_form.cleaned_data['message'],
#                 contact_type = contact_form.cleaned_data['contact_type'],
#                 subscription = contact_form.cleaned_data['subscription'],
#             )

#             new_message.save()
#             return redirect("contacto:send.html")

#         else:
#             print("El formulario NO es válido!")
#             # 4. Generamos el formulario con el que vamos a trabajar
#             contact_form = ContactForm()
#         """

#     if request.method == "POST":
#         contact_form = ContactForm(request.POST)
#         if contact_form.is_valid():
#             new_message = contact_form.save()
#             print(new_message)
#             return redirect("contacto:contact_page")
#         else:
#             print("El formulario NO es válido!")
#     else:
#         contact_form = ContactForm()

#     return render(request, "contactForm.html", { 'form': contact_form })
