from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *
urlpatterns=[
    path('',homepage,name='home'),
    path('product_list/<int:firm_id>/',product_list,name='product_list'),
    path('models/<int:product_id>/',product_models,name='product_models')
]