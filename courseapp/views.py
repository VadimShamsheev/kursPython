from django.shortcuts import render
from django.views import View


class GuestPage(View):
    def get(self, request):
        context = {}
        return render(request, 'index.html', context=context)


class RegisterPage(View):
    def get(self, request):
        return render(request, 'register_form.html')


class AuthorizePage(View):
    def get(self, request):
        return render(request, 'authorize_form.html')


class MasterPage(View):
    def get(self, request):
        return render(request, 'master_page.html')


class AdminPageOrder(View):
    def get(self, request):
        return render(request, 'admin_page.html')


class AdminPageService(View):
    def get(self, request):
        return render(request, 'admin_page_services.html')


class CreateOrder(View):
    def get(self, request):
        return render(request, 'create_order.html')


class EditService(View):
    def get(self, request):
        return render(request, 'edit_service.html')
