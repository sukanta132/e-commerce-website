from django.contrib import admin
from user_profile.models import UserProfile
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display=[
        'user',
        'mobile',
        'address'
    ]
    search_fields=[
        'user',
        'mobile',
        'address'
    ]
    list_filter=[
        'user',
        'mobile',
        'address'
    ]
admin.site.register(UserProfile, UserProfileAdmin)