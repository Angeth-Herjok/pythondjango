from django.contrib import admin
from .models import Order

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    total_display = ("purchaser_name","purchaser_numbe","vender_name","vender_number","product_description","price","quantity")
admin.site.register(Order,OrderAdmin)
    