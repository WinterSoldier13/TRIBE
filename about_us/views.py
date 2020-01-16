from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def load(request):
    return render(request,'about_us/about_us.html')