from django.contrib import admin


# Register your models here.
from .models import Location
class LocationAdmin(admin.ModelAdmin):
    total_display = ("location_name","latitude","longitude","Address")
admin.site.register(Location,LocationAdmin)
    

