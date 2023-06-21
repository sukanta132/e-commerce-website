from django.shortcuts import render, redirect
from cms.models import Slider, WebsiteSetting, Blog, Testimonial
from product.models import ProductCategory, Product, ProductTag
from django.views import View
from django.contrib import admin, messages
from frontend.models import ContactUs
from order.models import OrderDetails, Order
# Create your views here.

def home_page(request):
    ''' home page of k-mart E-com '''
    testimonial_one = Testimonial.objects.filter(status=True)[0:1]
    testimonial_two = Testimonial.objects.filter(status=True)[1:2]
    blog = Blog.objects.filter(status=True)
    # Website_Setting = WebsiteSetting.objects.all().last() # replaced with context processor
    # navigation_categories = ProductCategory.objects.filter(status=True) # replaced with conyext processor
    sliders = Slider.objects.filter(status=True)
    Product_Categories = ProductCategory.objects.filter(status=True)[0:5]
    fashion_product_one = Product.objects.select_related('product_category').filter(status=True)[0:2]
    fashion_product_two = Product.objects.select_related('product_category').filter(status=True)[2:4]
    product_tag = ProductTag.objects.filter(status=True)[0:2]
    context = {
        'testimonial_one' : testimonial_one,
        'testimonial_two' : testimonial_two,
        'blog' : blog,
        # 'Website_logo' : Website_Setting, # replaced with context processor
        # 'navigation_categories' : navigation_categories, # replaced with context processor
        'sliders' : sliders,
        'Product_Categories' : Product_Categories,
        'fashion_product_one' : fashion_product_one,
        'fashion_product_two' : fashion_product_two,
        'product_tag' : product_tag,

    }
    print(context)
    return render(request, 'home.html', context)


def about_page(request):
    return render(request, 'about.html')


def contact_page(request):
    if request.method=="POST":
        vName = request.POST.get('name')
        vEmail = request.POST.get('email')
        vPhone = request.POST.get('phone')
        vMessage = request.POST.get('message')
        us = ContactUs(name=vName, email=vEmail, phone_number=vPhone, message=vMessage)
        print(us)
        us.save()
        return redirect('home_page')
    return render(request, 'contact.html')

""" products with category id """
# def product_listing(request, category_id):
    #product_category = Product.objects.all().filter(status=True, product_category_id=category_id) #recomended
    #product_category = Product.objects.all().filter(status=True, product_category=category_id)
    # print(product_category)
    # Website_Setting = WebsiteSetting.objects.all().last()
    # navigation_categories = ProductCategory.objects.filter(status=True)
    # context = {
    #     'Website_logo' : Website_Setting,
    #     'navigation_categories' : navigation_categories,
    #     'product_category' : product_category

    # }
    # return render(request, 'product/product_listing.html', context)

""" products with category slug """
def product_listing(request, product_category_slug=None):
    filters = {
        'status':True
    }
    print(request.GET)
    if request.GET.get('search'):
        filters['name__icontains'] = request.GET.get('search')

    if product_category_slug:
        filters['product_category__slug'] = product_category_slug
    print(filters)
    product_category = Product.objects.all().filter(**filters) #recomended , filter(status=True, product_category__slug=product_category_slug) it removed for serch
    # print(product_category_slug)
    # print(product_category)
    # Website_Setting = WebsiteSetting.objects.all().last() # replaced with context processor
    # navigation_categories = ProductCategory.objects.filter(status=True) # replaced with context processor
    context = {
        # 'Website_logo' : Website_Setting, # replaced with context processor
        # 'navigation_categories' : navigation_categories, # replaced with context processor
        'product_category' : product_category

    }
    return render(request, 'product/product_listing.html', context)

''' class based view '''
class ProductDetails(View):

    def get(self, request, product_slug):
        # Website_Setting = WebsiteSetting.objects.all().last()
        # navigation_categories = ProductCategory.objects.filter(status=True)
        # product_slug = 'denim-jacket'
        # print(product_slug)
        try:
           
           product = Product.objects.get(slug=product_slug)
           similar_products = Product.objects.filter(status=True, product_category=product.product_category) 
           context = {
            #    'Website_logo' : Website_Setting,
            #    'navigation_categories' : navigation_categories,
               'product' : product,
               'similar_products' : similar_products,

                }
           return render(request, 'product/product_details.html', context)
        except Product.DoesNotExist:
            pass
       

def order_history(request):
    order_history = OrderDetails.objects.filter(status=True)
    order_status = Order.objects.all()
    context = {
        'order_history': order_history,
        'order_status': order_status,
    }
    return render(request, 'order/order_history.html', context)


def blog_view(request):
    blog = Blog.objects.filter(status=True)
    context = {
        'blog': blog,
    }
    return render(request, 'blog/blog.html', context)