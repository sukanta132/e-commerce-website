from django.db import models
from django.contrib.auth.models import User
from product.models import Product, ProductVariation
# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    variation = models.ForeignKey(ProductVariation,  on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='media/order', null=True)

    def __str__(self):
        return f"{self.user} {self.quantity}"
    

