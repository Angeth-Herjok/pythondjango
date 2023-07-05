from django.contrib import admin
from .models import Reviews

# Register your models here.
class ReviewsAdmin(admin.ModelAdmin):
    total_display = ("name","comment")
admin.site.register(Reviews,ReviewsAdmin)
    