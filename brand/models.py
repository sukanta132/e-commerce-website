from django.db import models

# Create your models here.


class Brand(models.Model):
    """ model class for brrand """
    name = models.CharField(max_length=255)
    status = models.BooleanField(default=True)

    def __str__(self):
        """ string representation of object brand """
        return self.name