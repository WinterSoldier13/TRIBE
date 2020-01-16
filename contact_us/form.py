from django import forms

class feedback_form(forms.Form):
    email = forms.EmailField(label='your email')
    text = forms.CharField(label="Input your suggestions here", max_length=1000)

