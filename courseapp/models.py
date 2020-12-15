from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Employee(models.Model):
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=30, default="")
    name = models.CharField(max_length=100)
    privilege = models.CharField(max_length=10, default="customer")
    phone = models.CharField(max_length=11, blank=True)
    discount = models.IntegerField(default=0, blank=True)
    qualification = models.IntegerField(default=0, blank=True)
    picture = models.ImageField(upload_to="static/images", blank=True)
    description = models.TextField(default="", blank=True)


class Service(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField(default=0)
    lead_time = models.IntegerField(default=0)


class Order(models.Model):
    date_time = models.DateTimeField(default=timezone.now)
    master_id = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="master_id")
    customer_id = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="customer_id")
    service = models.ManyToManyField(Service, related_name="service_rel")
    status = models.CharField(max_length=10, default="accepted")
    cost = models.IntegerField(default=0)
