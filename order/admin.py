from django.contrib import admin, messages
from order.models import Order, OrderDetails
# Register your models here.

class OrderDetailsInline(admin.TabularInline):
    ''' display child form in table format '''
    model = OrderDetails

def active_payment(modelAdmin, request, queryset):
    queryset.update(payment = True)
    messages.success(request, "selected record(s) marked as active")

def inactive_payment(modelAdmin, request, queryset):
    queryset.update(payment = False)
    messages.success(request, "selected record(s) marked as inactive")

class OrderAdmin(admin.ModelAdmin):
    list_display=[
        'user',
        'date_time',
        'address',
        'mobile',
        'payment',
        'status'
    ]

    search_fields=[
        'mobile'
    ]

    list_filter=[
        'user',
        'address',
        'mobile'
    ]
    inlines = (OrderDetailsInline,)
    actions = (active_payment, inactive_payment)
admin.site.register(Order, OrderAdmin)


class OrderDetailsAdmin(admin.ModelAdmin):
    list_display=[
        'order',
        'product',
        'quantity',
        'price',
        'Total_price',
        'status',
        'variation',
    ]

    search_fields=[
        'product'
    ]

    list_filter=[
        'order',
        'product'
    ]
admin.site.register(OrderDetails, OrderDetailsAdmin)