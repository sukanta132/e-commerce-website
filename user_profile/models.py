from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    mobile = models.CharField(max_length=12, null=True)
    address = models.TextField(null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    

    ''' when user model is saved create_profile will receive a signal
        examples of signals: post_save, pre_save, post_delete, ptre_delete
    
    '''

from django.dispatch import receiver
from django.db.models.signals import post_save

@receiver(post_save, sender=User)
def crteate_profile(sender, instance, created, **kwargs):
    ''' operations '''
    if created:
        UserProfile.objects.create(user=instance)



    # print("Signal Reiceved")
    # print(sender)
    # print(instance)
    # print(created)