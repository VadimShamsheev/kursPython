from ..models import Employee, Service, Order
from django.contrib.auth.models import User
from django.core.exceptions import *
from datetime import datetime


def get_masters():
    masters = Employee.objects.filter(privilege="master")
    return masters


def get_customers():
    customers = Employee.objects.filter(privilege="customer")
    return customers


def get_user(login, password):
    try:
        user = Employee.objects.get(login=login, password=password)
        return user
    except ObjectDoesNotExist:
        return None


def get_orders_for_master(master_id):
    date = datetime.today().strftime("%Y-%m-%d")
    orders = Order.objects.filter(master_id=master_id, date_time__date=date).prefetch_related('service').order_by('date_time')
    print(date)
    return orders


def get_orders():
    orders = Order.objects.filter(status='accepted').order_by('date_time')
    return orders


def get_orders_filter(master, start_date, end_date):
    st_date = str('2000-01-01 00:00')
    e_date = str('2050-01-01 00:00')
    if start_date != '':
        st_date = start_date.replace('T', ' ')

    if end_date != '':
        e_date = end_date.replace('T', ' ')

    if not master or master == 'none':
        orders = Order.objects.filter(status='accepted', date_time__range=[st_date, e_date]).order_by('date_time')
    else:
        orders = Order.objects.filter(status='accepted', master_id=master, date_time__range=[st_date, e_date]).order_by('date_time')
    print("Start: " + st_date)
    print("End: " + e_date)
    return orders


def get_order(order_id):
    order = Order.objects.get(id=order_id)
    return order


def get_services():
    services = Service.objects.all()
    return services


def get_service_by_id(service_id):
    service = Service.objects.get(id=service_id)
    return service


def get_user_by_id(id):
    try:
        user = Employee.objects.get(id=id)
    except ObjectDoesNotExist:
        user = None
    return user


def find_user_by_login(login):
    user = Employee.objects.filter(login=login.lower())
    return user


def add_user(login, password, name):
    user = Employee(name=name.lower(), login=login.lower(), password=password.lower())
    user.save()


def add_order(date, time, customer, master, services, price):
    order = Order(date_time=date+' '+time, customer_id=customer, master_id=master, cost=price)
    order.save()
    for service in services:
        order.service.add(Service.objects.get(id=service))


def update_service(service_id, name, price, lead_time):
    service = Service.objects.get(id=service_id)
    service.name = name
    service.price = price
    service.lead_time = lead_time
    service.save()


def update_order(order_id, date, time, customer, master, services, status):
    order = Order.objects.get(id=order_id)
    order.date_time = date+" "+time
    order.customer_id = customer
    order.master_id = master
    order.status = status
    order.save()
    for service in services:
        order.service.add(service)
