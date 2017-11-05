from django import forms

class HealthInsuranceInputForm(forms.Form):
    zipcode = forms.CharField(label='Your zip code', max_length=100)
