from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'subject', 'email')


admin.site.register(Contact, ContactAdmin)