from django.contrib import admin
from frontend.models import ContactUs
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'email', 'message']
admin.site.register(ContactUs, ContactAdmin)

