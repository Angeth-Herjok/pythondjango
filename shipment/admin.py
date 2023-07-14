from django.contrib import admin
from .models import Shipment

# Register your models here.
class ShipmentAdmin(admin.ModelAdmin):
    total_display = ("tracking_number","status","date_craeted","date_shipped")
admin.site.register(Shipment,ShipmentAdmin)
