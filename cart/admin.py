from django.contrib import admin
from .models import Cart

# Register your models here.
class CartAdmin(admin.ModelAdmin):
    total_display = ("product_name","product_pric","quantity","product_id","imag","date_added")
admin.site.register(Cart,CartAdmin)

