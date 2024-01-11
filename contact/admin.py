from django.contrib import admin
from .models import Contact

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'surname', 'email', 'contact_type', 'message', 'subscription', 'created_at')
    search_fields=('id', 'name', 'email', 'message')
    list_filter=('name', 'email','contact_type','subscription', 'created_at')
