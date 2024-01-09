from django import forms

from .models import Category

class ProductForm(forms.Form):
    name = forms.CharField(label="Nombre",required=True, max_length=100, min_length=3)
    description = forms.CharField(label="Descripción", max_length=255, min_length=10, required=True, widget=forms.Textarea)
    price = forms.FloatField(label="Precio", required=True, min_value=0.99, max_value=4500)
    category = forms.ModelChoiceField(label="Categoría", required=True, queryset=Category.objects.all())
