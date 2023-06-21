from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home_page, name="home_page"),
    path('about', views.about_page, name="about_page"),
    path('contact', views.contact_page, name="contact_page"),
    # path('product_listing/<category_id>', views.product_listing, name="product_listing"),
    path('product_listing/', views.product_listing, name="product_listing"),
    path('product_listing/<slug:product_category_slug>', views.product_listing, name="product_listing"),
    path('product-details/<slug:product_slug>', views.ProductDetails.as_view(), name="ProductDetails"),
    path('order_history', views.order_history, name="order_history"),
    path('blog', views.blog_view, name="blog_view"),



]