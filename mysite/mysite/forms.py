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

INN_MOOP_CHOICES = (
    (0,'0-100'),
    (1,'101-500'),
    (2,'501-2000'),
    (3,'2001+'),
)

OON_MOOP_CHOICES = (
    (0,'0-100' ),
    (1,'101-1000' ),
    (2,'1001-10000' ),
    (3,'10000+'  ),
)

INN_DED_CHOICES = (
    (0,'0-100' ),
    (1,'101-500' ),
    (2,'501-2000' ),
    (3,'2001+'  ),
)

OON_DED_CHOICES = (
    (0,'0-100' ),
    (1,'101-1000'),
    (2,'1001-10000'),
    (3,'10000+'),
)

INN_COINSURANCE_CHOICES = (
    (0,'0-25'),
    (1,'26-50'),
    (2,'51-75'),
    (3,'76-100'),
)


class HealthInsuranceInputForm(forms.Form):
    # hard filters
    zipcode = forms.CharField(label='Zip Code', max_length=100)
    age = forms.IntegerField(label='Age')
    months_tobacco_free = forms.IntegerField(label='Number of Months Tobacco Free')
    # soft filters
    diseases = forms.MultipleChoiceField(choices=DISEASE_CHOICES, widget=forms.CheckboxSelectMultiple())
    desired_premium_price = forms.IntegerField(label='Desired Premium Price')
    desired_in_network_out_of_pocket_maximum = forms.ChoiceField(choices=INN_MOOP_CHOICES, widget=forms.RadioSelect())
    desired_out_of_network_out_of_pocket_maximum = forms.ChoiceField(choices=OON_MOOP_CHOICES, widget=forms.RadioSelect())
    desired_in_network_deductible = forms.ChoiceField(choices=INN_DED_CHOICES, widget=forms.RadioSelect())
    desired_out_of_network_deductible = forms.ChoiceField(choices=OON_DED_CHOICES, widget=forms.RadioSelect())
    desired_in_network_coinsurance = forms.ChoiceField(choices=INN_COINSURANCE_CHOICES, widget=forms.RadioSelect())

