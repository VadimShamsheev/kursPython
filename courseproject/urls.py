"""courseproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from courseapp.views import GuestPage, MasterPage, AdminPageOrder, AdminPageService, CreateOrder, EditService, \
    RegisterPage, AuthorizePage

urlpatterns = [
    path('', GuestPage.as_view()),
    path('master_page.html', MasterPage.as_view()),
    path('register_form.html', RegisterPage.as_view()),
    path('authorize_form.html', AuthorizePage.as_view()),
    path('create_order.html', CreateOrder.as_view()),
    path('edit_service.html', EditService.as_view()),
    path('admin_page.html', AdminPageOrder.as_view()),
    path('admin_page_services.html', AdminPageService.as_view()),
    path('authorize_form.html', AuthorizePage.as_view()),
]