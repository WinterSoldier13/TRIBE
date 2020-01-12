from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test_request(request):
    return HttpResponse('<h1>This is the HOME page</h1>')