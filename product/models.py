from django.db import models
from django.template.defaultfilters import slugify
from brand.models import Brand
# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='media/product_category')
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        ''' overriding save method of super model'''
        # print(self.name)
        self.slug = slugify(self.name)
        super(ProductCategory, self).save(*args, **kwargs)
        
    

class ProductVariation(models.Model):
    name = models.CharField(max_length=255)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

class ProductTag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        ''' overriding save method of super model '''
        # print(self.name)
        self.slug = slugify(self.name)
        super(ProductTag, self).save(*args, **kwargs) #save object
    

class Product(models.Model):
    product_category = models.ForeignKey(ProductCategory, related_name='product_category', on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    cover_image = models.ImageField(upload_to='media/products')
    price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField()
    variation = models.ManyToManyField(ProductVariation)
    tags = models.ManyToManyField(ProductTag)
    stock = models.IntegerField(default=1)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        ''' overriding save method of super model '''
        # print(self.name)
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs) #save object


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="ProductImage")
    image = models.ImageField(upload_to='media/products') 

    def __str__(self):
        return str(self.id)


