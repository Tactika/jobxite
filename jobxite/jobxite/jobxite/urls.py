"""jobxite URL Configuration

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
from django.contrib import admin
from django.urls import path
from apps.core.views import index, contact, rentals, sales, loginPage, registerPage, logout_user, item_list

urlpatterns = [
    path('', index, name='index'),
    path('rentals/', rentals, name='rentals'),
    path('item_list/', item_list, name='item_list'),
    path('sales/', sales, name='sales'),
    path('contact/', contact, name='contact'),
    path('login/', loginPage, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', registerPage, name='register'),
    path('admin/', admin.site.urls),
]
