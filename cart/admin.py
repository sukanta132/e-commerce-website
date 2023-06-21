from django.contrib import admin
from cart.models import Cart
# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display=[
        'user',
        'product',
        'variation',
        'quantity'
    ]

    search_fields=[
        'user__username'
    ]

    list_filter=[
        'user',
        'product'
    ]
admin.site.register(Cart, CartAdmin)