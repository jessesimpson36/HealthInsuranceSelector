from django import forms
import sys
import os

BASE_DIR = os.getcwd()

sys.path.insert(0, os.path.join( os.getcwd(), "database") )
os.chdir(os.path.join( BASE_DIR, "database"))
import databasefunctions as dbf

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

BENEFIT_CHOICES = dbf.get_benefits("health_insurance.db")

INN_MOOP_CHOICES = (
    (0,'0-100'),
    (1,'101-500'),
    (2,'501-2000'),
    (3,'2001+'),
)

# OON_MOOP_CHOICES = (
#     (0,'0-100' ),
#     (1,'101-1000' ),
#     (2,'1001-10000' ),
#     (3,'10000+'  ),
# )

INN_DED_CHOICES = (
    (0,'0-100' ),
    (1,'101-500' ),
    (2,'501-2000' ),
    (3,'2001+'  ),
)

# OON_DED_CHOICES = (
#     (0,'0-100' ),
#     (1,'101-1000'),
#     (2,'1001-10000'),
#     (3,'10000+'),
# )

INN_COINSURANCE_CHOICES = (
    (0,'0-25'),
    (1,'26-50'),
    (2,'51-75'),
    (3,'76-100'),
)

YES_NO = (
    ("Yes", "Yes"),
    ("No", "No"),
)

YES_NO_ALTERNATIVE = (
    (1, "Yes"),
    (0, "No"),
)

class HealthInsuranceInputForm(forms.Form):
    # hard filters
    zipcode = forms.CharField(label='Zip Code', max_length=5, min_length=5)
    age = forms.IntegerField(label='Age', min_value=1, max_value=150)
    do_you_smoke = forms.ChoiceField(choices=YES_NO, widget=forms.RadioSelect, label="Do you smoke?")
    # soft filters
    benefits = forms.MultipleChoiceField(choices=BENEFIT_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False)
    diseases = forms.MultipleChoiceField(choices=DISEASE_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False)
    # importance_of_diseases = forms.IntegerField(max_value=10, min_value= 0, widget=forms.TextInput(attrs={'placeholder': '0-10'}), required=False)
    desired_premium_price = forms.IntegerField(label='Desired Premium Price', required=False)
    # importance_of_premium_prices = forms.IntegerField(max_value=10, min_value=0, widget=forms.TextInput(attrs={'placeholder': '0-10'}), required=False)
    desired_in_network_out_of_pocket_maximum = forms.IntegerField(help_text="0-975" , min_value=0, max_value=975, required=False)
    # importance_of_in_network_out_of_pocket_maximum = forms.IntegerField(max_value=10, min_value=0, widget=forms.TextInput(attrs={'placeholder': '0-10'}), required=False)
    desired_in_network_deductible = forms.IntegerField(help_text="0-950" , min_value=0, max_value=950, required=False)
    # importance_of_in_network_deductible = forms.IntegerField(max_value=10, min_value=0, widget=forms.TextInput(attrs={'placeholder': '0-10'}), required=False)
    desired_in_network_coinsurance = forms.IntegerField(help_text="0-100",min_value=1, max_value=150, required=False)
    # importance_of_in_network_coinsurance = forms.IntegerField(max_value=10, min_value=0, widget=forms.TextInput(attrs={'placeholder': '0-10'}), required=False)
    # premium, benefits, disease, coinsurance, copay, coinsurance, deductible, moop, visits, out of country?

    # these are inputs that Satvik requested:
    desired_copay = forms.IntegerField(label='Desired Copay', help_text="0-4500", min_value=0, max_value=4500, required=False)
    number_of_visits = forms.IntegerField(label='How many doctor visits do you typically have per month?', required=False)
    out_of_country = forms.ChoiceField(choices=YES_NO_ALTERNATIVE, widget=forms.RadioSelect)

class BasicHealthInsuranceInfo():
    issuer_name = "ERROR"
    plan_name = "ERROR"
    premium_price = 99999
    issuer_id = "ERROR"
    plan_id = "ERROR"
    copay = "ERROR"
    coinsurance = "ERROR"
    brochure_link = "ERROR"
    enrollment_link = "ERROR"
    bbb_rating = "ERROR"
    customer_rating = "ERROR"
    out_of_country = "ERROR"
    diseases = []
    moop = "ERROR"
    benefits = []
    pos_count = 0
    neg_count = 0
    high_count = 0
    low_count = 0


if __name__ != "__main__":
    os.chdir(os.path.join(".."))
