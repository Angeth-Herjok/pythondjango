from django.contrib import admin
from .models import Payment
# Register your models here.
class PaymentAdmin(admin.ModelAdmin):
    total_display = ("payee_name","payee_address","payment_amount")
admin.site.register(Payment,PaymentAdmin)
