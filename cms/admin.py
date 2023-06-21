from django.contrib import admin, messages
from cms.models import Blog, FAQs, Slider, WebsiteSetting, Testimonial
# Register your models here.

def active_status(modelAdmin, request, queryset):
    queryset.update(staus  = True)
    messages.success(request, "selected record(s) marked as active")

def inactive_status(modelAdmin, request, queryset):
    queryset.update(staus  = False)
    messages.success(request, "selected record(s) marked as inactive")


class BlogAdmin(admin.ModelAdmin):
    list_display=['title', 'description', 'status', 'author','image', 'date_time' ]
    search_fields=['title']
    list_filter=['title']
    actions = (active_status, inactive_status)

admin.site.register(Blog, BlogAdmin)


class WebsiteSettingAdmin(admin.ModelAdmin):
    list_display=['title', 'email', 'phone']

admin.site.register(WebsiteSetting, WebsiteSettingAdmin)


class SliderAdmin(admin.ModelAdmin):
    list_display=['heading', 'sub_heading', 'image', 'status']
    search_fields=['heading']
    list_filter=['heading']

admin.site.register(Slider, SliderAdmin)


class FAQsAdmin(admin.ModelAdmin):
    list_display=['question', 'answer', 'status']
    search_fields = ['question']
    list_filter = ['status']
admin.site.register(FAQs, FAQsAdmin)


def active_status(modelAdmin, request, queryset):
    queryset.update(status=True)
    messages.success(request, "selected record(s) marked as active")

def inactive_status(modelAdmin, request, queryset):
    queryset.update(status=False)
    messages.success(request, "selected record(s) marked as inactive")


class TestimonialAdmin(admin.ModelAdmin):
    list_display=['name', 'description', 'image', 'status']
    list_filter=['status']
    search_fields=['name']
    actions=(active_status, inactive_status)
admin.site.register(Testimonial, TestimonialAdmin)