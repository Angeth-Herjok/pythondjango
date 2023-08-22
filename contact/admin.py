from django.contrib import admin

# Register your models here.
from .models import Contact
class ContactAdmin(admin.ModelAdmin):
    total_display = ("full_name","phone_number","email","social_media_links")
admin.site.register(Contact,ContactAdmin)
    
