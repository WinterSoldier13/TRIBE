from django.shortcuts import render


# Create your views here.

def load(request):
    return render(request,'contact_us/contact.html')