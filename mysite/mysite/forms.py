from django import forms

DISEASE_CHOICES = (
    ('asthma', 'Asthma'),
    ('depression', 'Depression'),
    ('diabetes', 'Diabetes'),
    ('heart disease', 'Heart Disease'),
    ('high blood pressure or high cholesterol', 'High Blood Pressure or High Cholesterol'),
    ('low back pain', 'Low Back Pain'),
    ('pain management', 'Pain Management'),
    ('pregnancy', 'Pregnancy'),
    ('weight loss programs', 'Weight Loss Programs'),

)

class HealthInsuranceInputForm(forms.Form):
    # hard filters
    zipcode = forms.CharField(label='Zip Code', max_length=100)
    age = forms.IntegerField(label='Age')
    months_tobacco_free = forms.IntegerField(label='Number of Months Tobacco Free')
    # soft filters
    diseases = forms.MultipleChoiceField(choices=DISEASE_CHOICES, widget=forms.CheckboxSelectMultiple())
    desired_premium_price = forms.IntegerField(label='Desired Premium Price')
    out_of_pocket_maximum = forms.IntegerField(label='Desired Out of Pocket Maximum')
    deductible = forms.IntegerField(label='Desired Deductible')
