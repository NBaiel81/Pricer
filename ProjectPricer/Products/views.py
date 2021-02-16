from django.shortcuts import render

from .models import *
def homepage(request):
    products = Product.objects.all()
    return render(request, 'products/homepage.html', {'products': products})

