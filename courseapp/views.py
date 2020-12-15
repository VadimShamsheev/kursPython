from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from datetime import datetime

from .pythonScripts.getData import *


class GuestPage(View):
    def get(self, request):
        request.session['user_id'] = 0
        request.session['user_privilege'] = ""
        masters = get_masters()
        services = get_services()
        context = {
            "masters": masters,
            "services": services,
        }
        return render(request, 'index.html', context=context)


class CustomerPage(View):
    def get(self, request):
        masters = get_masters()
        services = get_services()
        context = {
            "masters": masters,
            "services": services,
        }
        return render(request, 'customer_page.html', context=context)


class RegisterPage(View):
    def get(self, request):
        return render(request, 'register_form.html')

    def post(self, request):
        context = {}
        login = request.POST.get("reg_login")
        password = request.POST.get("reg_pass")
        name = request.POST.get("reg_name")

        if not login:
            context["login_message"] = "Поле обязательное"
        if not password:
            context["pass_message"] = "Поле обязательное"
        if not name:
            context["name_message"] = "Поле обязательное"
        if context:
            context["login"] = login
            context["name"] = name
            return render(request, 'register_form.html', context=context)

        else:
            if find_user_by_login(login):
                context['name'] = name
                context["message"] = "Данный пользователь уже существует в системе"
                return render(request, 'register_form.html', context=context)
            else:
                add_user(login, password, name)
                user = get_user(login, password)
                print(user)
                request.session['user_id'] = get_user(login, password).id
                request.session['user_privilege'] = get_user(login, password).privilege
                return HttpResponseRedirect('customer_page.html')


class AuthorizePage(View):
    def get(self, request):
        return render(request, 'authorize_form.html')

    def post(self, request):
        login = request.POST.get('auth_login')
        password = request.POST.get('auth_pass')
        user = get_user(login, password)
        if not user:
            context = {
                "message": 'Введен неверный логин или пароль',
                "login": login,
            }
            return render(request, 'authorize_form.html', context=context)
        else:
            request.session['user_id'] = user.id
            request.session['user_privilege'] = user.privilege
            if user.privilege == "master":
                return HttpResponseRedirect('master_page.html')
            elif user.privilege == "admin":
                return HttpResponseRedirect('admin_page.html')
            else:
                return HttpResponseRedirect('customer_page.html')


class MasterPage(View):
    def get(self, request):
        if request.session['user_id'] is None:
            return HttpResponseRedirect('authorize_form.html')
        else:
            orders = get_orders_for_master(request.session['user_id'])
            context = {
                "orders": orders,
                "today_date": datetime.now(),
            }
            return render(request, 'master_page.html', context=context)


class AdminPageOrder(View):
    def get(self, request):
        orders = get_orders()
        masters = get_masters()
        context = {
            "orders": orders,
            "masters": masters,
        }
        return render(request, 'admin_page.html', context=context)

    def post(self, request):
        masters = get_masters()
        master = request.POST.get('filter_master')
        start_date = request.POST.get('filter_start_date')
        end_date = request.POST.get('filter_end_date')
        orders = get_orders_filter(master, start_date, end_date)
        context = {
            "orders": orders,
            "masters": masters,
        }
        return render(request, 'admin_page.html', context=context)


class AdminPageService(View):
    def get(self, request):
        services = get_services()
        context = {
            "services": services,
        }
        return render(request, 'admin_page_services.html', context=context)


class CreateOrder(View):
    def get(self, request):
        if request.session['user_privilege'] == "":
            return HttpResponseRedirect('authorize_form.html')
        elif request.session['user_privilege'] == "admin":
            masters = get_masters()
            customers = get_customers()
            services = get_services()
            context = {
                "masters": masters,
                "customers": customers,
                "services": services,
                "user_privilege": request.session['user_privilege'],
            }
            return render(request, 'create_order.html', context=context)
        elif request.session['user_privilege'] == "master":
            return HttpResponseRedirect('master_page.html')
        elif request.session['user_privilege'] == "customer":
            masters = get_masters()
            services = get_services()
            user = get_user_by_id(request.session['user_id'])
            context = {
                "masters": masters,
                "services": services,
                "customers": user,
                "user_privilege": request.session['user_privilege'],
            }
            return render(request, 'create_order.html', context=context)

    def post(self, request):
        context = {}
        service = request.POST.getlist('create_service_name')
        date = request.POST.get('create_order_date')
        time = request.POST.get('create_order_time')
        customer_id = request.POST.get('create_order_customer')
        customer = get_user_by_id(customer_id)
        master_id = request.POST.get('create_order_master')
        master = get_user_by_id(master_id)
        cost = request.POST.get('order_cost')
        print(request.POST.get('create_order_customer'))
        add_order(date, time, customer, master, service, cost)
        if (request.session['user_privilege']) == "customer":
            return HttpResponseRedirect('customer_page.html')
        else:
            return HttpResponseRedirect('admin_page.html')


class EditOrder(View):
    def get(self, request, order_id):
        if request.session['user_privilege'] == "admin":
            statuses = {
                'accepted': 'Принят',
                "done": "Завершен",
                'canceled': 'Отменен',
            }
            time_work = [
                '10:00',
                '11:00',
                '12:00',
                '13:00',
                '14:00',
                '15:00',
                '16:00',
                '17:00',
                '18:00',
                '19:00',
                '20:00'
            ]
            order = get_order(order_id)
            services = get_services()
            masters = get_masters()
            customers = get_customers()
            context = {
                "time_work": time_work,
                "order": order,
                "services": services,
                "customers": customers,
                "masters": masters,
                "statuses": statuses,
            }
            return render(request, 'edit_order.html', context=context)
        else:
            return HttpResponseRedirect('/')

    def post(self, request, order_id):
        context = {}
        service = request.POST.getlist('create_service_name')
        date = request.POST.get('create_order_date')
        time = request.POST.get('create_order_time')
        customer_id = request.POST.get('create_order_customer')
        customer = get_user_by_id(customer_id)
        master_id = request.POST.get('create_order_master')
        master = get_user_by_id(master_id)
        status = request.POST.get('create_order_status')
        update_order(order_id, date, time, customer, master, service, status)
        return HttpResponseRedirect('../admin_page.html')


class EditService(View):
    def get(self, request, service_id):
        service = get_service_by_id(service_id)
        context = {
            "service": service,
        }
        return render(request, 'edit_service.html', context=context)

    def post(self, request, service_id):
        context = {}
        serv_id = service_id
        service_name = request.POST.get('service_name')
        service_price = request.POST.get('service_price')
        service_dur = request.POST.get('service_dur')
        if not service_name:
            context['name_message'] = "Поле обязательное"
        if not service_price:
            context['price_message'] = "Поле обязательное"
        if not service_dur:
            context['dur_message'] = "Поле обязательное"

        if context:
            return render(request, 'edit_service.html', context=context)
        else:
            update_service(serv_id, service_name, service_price, service_dur)
            return HttpResponseRedirect('../admin_page_services.html')
