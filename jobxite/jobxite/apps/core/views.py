from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from apps.store.models import Product


# Create your views here.
def index(request):
    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, 'index.html')


def rentals(request):
    return render(request, 'rentals.html')


def sales(request):
    return render(request, 'sales.html')


def contact(request):
    return render(request, 'contact.html')

def logout_user(request):
    logout(request)
    return redirect('index')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
    return render(request, 'login.html')


def registerPage(request):
    form = UserCreationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
        else:
            form = UserCreationForm()
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
