from django.shortcuts import render

from .models import *
def homepage(request):
    firms = Firm.objects.all()
    return render(request, 'products/homepage.html', {'firms': firms})

def product_list(request,firm_id):
    firm = Firm.objects.get(id=firm_id)
    products= firm.product_set.all
    return render(request, 'products/product_list.html', {'products': products})

