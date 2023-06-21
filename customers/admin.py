from django.contrib import admin
from .models import Customers

# Register your models here.
class CustomersAdmin(admin.ModelAdmin):
    total_display = ("first_name","second_name","age","gender")
admin.site.register(Customers,CustomersAdmin)
    