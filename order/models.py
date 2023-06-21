from django.db import models
from django .contrib.auth.models import User
from product.models import Product, ProductVariation
# Create your models here.

class Order(models.Model):
    STATUS_CHOICE = (
        ('pending', 'pending'),
        ('inprogress', 'inprogress'),
        ('dispatch', 'dispatch'),
        ('delivered', 'delivered'),
        ('canceled', 'canceled'),
        ('rejected', 'rejected'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    address = models.TextField()
    mobile = models.CharField(max_length=12)
    payment = models.BooleanField(default=False)
    status = models.CharField(max_length=50, choices=STATUS_CHOICE)


    def __str__(self):
        return str(self.id)
    

class OrderDetails(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    variation = models.ForeignKey(ProductVariation,  on_delete=models.SET_NULL, null=True)
    Total_price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    status = models.BooleanField(default=True)
    # image = models.ImageField(upload_to='media/order', null=True)


    def __str__(self):
        return f"{self.order.id} {self.product}"
    
    class Meta:
        verbose_name = "OrderDetails"
        verbose_name_plural = "OrderDetails"
    

