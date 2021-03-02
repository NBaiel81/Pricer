from django.shortcuts import render
from .filters import Product_filter

from .models import *


def homepage(request):
    footers = Footer.objects.all()
    firms = Firm.objects.all()
    products = Product.objects.all()
    filters = Product_filter(request.GET, queryset=products)
    products = filters.qs
    return render(request, 'products/homepage.html', {'firms': firms, 'products':products, 'filters':filters,'footers':footers})


def product_list(request,firm_id):
    footers = Footer.objects.all()
    firm = Firm.objects.get(id=firm_id)
    products= firm.product_set.all()
    for i in products:
        print(i.product_model.all().count())
    filters = Product_filter(request.GET, queryset=products)
    products = filters.qs
    return render(request, 'products/product_list.html', {'products': products,'filters':filters,'footers':footers})


def product_models(request,product_id):
    footers = Footer.objects.all()
    product = Product.objects.get(id=product_id)
    p_models = product.product_model.all()
    return render(request, 'products/product_detail.html', {'product': product,'models':p_models,'footers':footers})

