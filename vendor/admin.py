from django.contrib import admin

# Register your models here.
from .models import Vender
class VenderAdmin(admin.ModelAdmin):
    total_display = ("first_name","second_name","age","gender")
admin.site.register(Vender,VenderAdmin)
