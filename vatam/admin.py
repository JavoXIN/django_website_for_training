from django.contrib import admin
from .models import Order, StatusVatam, ComentVatam
# Register your models here.

admin.site.register(Order)
admin.site.register(StatusVatam)
admin.site.register(ComentVatam)
