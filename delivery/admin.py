from django.contrib import admin
from .models import Delivery

# Register your models here.
class DeliveryAdmin(admin.ModelAdmin):
    total_display = ("company_name","recipient_name","shipper","delivery_order_number")
admin.site.register(Delivery,DeliveryAdmin)
    
