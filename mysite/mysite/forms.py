from django import forms

class HealthInsuranceInputForm(forms.Form):
    zipcode = forms.CharField(label='Your zip code', max_length=100)

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)