from django.contrib import admin, messages
from product.models import ProductCategory, ProductVariation, ProductTag, Product, ProductImage
# Register your models here.


def active_status(modelAdmin, request, queryset):
    queryset.update(status = True)
    messages.success(request, "selected record(s) marked as active")

def inactive_status(modelAdmin, request, queryset):
    queryset.update(status = False)
    messages.success(request, "selected record(s) marked as inactive")

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display=['name', 'slug', 'image', 'status']
    search_fields=[ 'name' ]
    list_filter=[ 'name' ]
    actions = (active_status, inactive_status)

admin.site.register(ProductCategory, ProductCategoryAdmin)


def active_status(modelAdmin, request, queryset):
    queryset.update(status = True)
    messages.success(request, "selected record(s) marked as active")

def inactive_status(modelAdmin, request, queryset):
    queryset.update(status = False)
    messages.success(request, "selected record(s) marked as inactive")

class ProductVariationAdmin(admin.ModelAdmin):
    list_display=[ 'name', 'status' ]
    search_fields=[ 'name' ]
    list_filter=[ 'name' ]
    actions = (active_status, inactive_status)
admin.site.register(ProductVariation, ProductVariationAdmin)


def active_status(modelAdmin, request, queryset):
    queryset.update(status = True)
    messages.success(request, "selected record(s) marked as active")

def inactive_status(modelAdmin, request, queryset):
    queryset.update(status = False)
    messages.success(request, "selected record(s) marked as inactive")

class ProductTagAdmin(admin.ModelAdmin):
    list_display=[ 'name', 'slug', 'status' ]
    search_fields=[ 'name' ]
    list_filter=[ 'name' ]
    actions = (active_status, inactive_status)
admin.site.register(ProductTag, ProductTagAdmin)


class ProductImageInline(admin.TabularInline):
    ''' display child form in table format '''
    model = ProductImage
# class ProductImageInline(admin.StackedInline):
#     ''' display child form in row format '''
#     model = ProductImage
def active_status(modelAdmin, request, queryset):
    queryset.update(status = True)
    ''' messages.success -> shows green alert'''
    ''' messages.error -> shows red alert'''
    ''' messages.warning -> shows orange alert'''
    ''' messages.info -> shows green alert'''
    messages.success(request, "selected record(s) marked as active")

def inactive_status(modelAdmin, request, queryset):
    queryset.update(status = False)
    messages.success(request, "selected record(s) marked as inactive")

class ProductAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'slug' : ('name')}# for run time slug generate
    list_display=[ 'product_category', 'slug', 'name', 'cover_image', 'price', 'description', 'stock', 'status',
        # 'tag', <class 'product.admin.ProductAdmin'>: (admin.E108) The value of 'list_display[5]' refers to 'tag', which is not a callable, an attribute of 'ProductAdmin', or an attribute or method on 'product.Product'.    
    ]
    search_fields=[ 'name', 'price' ]
    list_filter=[ 'name', 'price' ]
    inlines = (ProductImageInline,)
    actions = (active_status, inactive_status)
admin.site.register(Product, ProductAdmin)


# class ProductImageAdmin(admin.ModelAdmin):
#     list_display=[
#         'product',
#         'image',
#     ]
#     search_fields=[
#         'product'
#     ]
#     list_filter=[
#         'product'
#     ]
# admin.site.register(ProductImage, ProductImageAdmin)