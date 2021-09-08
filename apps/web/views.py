from django.shortcuts import render
from.models import *
# Create your views here.
def index(request):
    allproduct = product.objects.all()
    return render(request, 'index.html', {'allproduct':allproduct})

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def productdetails(request):
    return render(request, 'product-details.html')

def shop(request):
    return render(request, 'shop.html')


