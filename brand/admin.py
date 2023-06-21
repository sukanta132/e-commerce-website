from django.contrib import admin
from brand.models import Brand
# Register your models here.

# admin.site.register(Brand)

class BrandAdmin(admin.ModelAdmin):
    list_display=[
        'name',
        'status'
    ]

    search_fields=[
        'name'
    ]

    list_filter=[
        'name'
    ]

admin.site.register(Brand, BrandAdmin)