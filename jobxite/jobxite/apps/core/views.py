from django.shortcuts import render
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