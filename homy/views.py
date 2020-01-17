from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.conf import settings
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import product

def index(request):
    prod=product.objects.all()
    #p1=product()
    #p1.name='Saree'
    #p1.oldprice=600
    #p1.newprice=300
    return render(request, 'shop.html',{'prod':prod})

