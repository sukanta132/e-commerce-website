from django.db import models

# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)
    message = models.TextField()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "ContactUs"
        verbose_name_plural = "ContactUs"