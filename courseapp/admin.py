from django.contrib import admin
from .models import Service, Employee, Order

# Register your models here.
admin.site.register(Service)
admin.site.register(Employee)
admin.site.register(Order)
