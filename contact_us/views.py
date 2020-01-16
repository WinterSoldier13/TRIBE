from django.shortcuts import render
from django.http import HttpResponse

from .form import feedback_form


# Create your views here.

def load(request):
    form = feedback_form(request.POST)

    if form.is_valid():  # All validation rules pass
        email = str(form.cleaned_data['email'])
        suggestions = str(form.cleaned_data['text'])
        print('FORM HERE>>>>>>>>>>> '+ email+'   '+suggestions)

        return HttpResponse('<h1>Thank you for your valuable Feedback</h1>')  # Redirect after POST
    return render(request, 'contact_us/contact.html', {'form': form})
