import sys
import os
import pandas as pd
sys.path.append('..')
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.http import HttpResponseRedirect
from django.conf import settings
BASE_DIR = os.getcwd()
print(BASE_DIR)
from .forms import HealthInsuranceInputForm
from .forms import *
# sys.path.append( os.path.join( BASE_DIR, "database") )
sys.path.insert(0, os.path.join( BASE_DIR , "database") )
os.chdir( os.path.join( BASE_DIR, "database"))
# os.chdir("/home/jesse/PycharmProjects/DDDM/mysite/database/")
print(os.getcwd())
print(sys.path)
import databasefunctions as dbf


# Create your views here.
def input(request):
    if request.method == 'POST':
        form = HealthInsuranceInputForm(request.POST)
        # print(form.zipcode)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            frame = dbf.hard_filters_pg1("health_insurance.db", form.data['zipcode'], form.data['age'], form.data['do_you_smoke'],
                                         form.data['diseases'], form.data['benefits'], form.data['desired_premium_price'])
            if form.data['do_you_smoke'] == "Yes":
            # normalize inputs (premium, copay, coinsurance, deductible, moop, visits)
            # the values obtained were found using database maxes and mins
                if ( form.data['desired_premium_price'] == 0):
                    premium = 0
                else:
                    premium = (form.data['desired_premium_price'] - 73 ) / ( 2673.63 - 73 )

            else:
                if ( form.data['desired_premium_price'] == 0):
                    premium = 0
                else:
                    premium = (form.data['desired_premium_price'] - 73.0 )/ (2314.71 - 73)

            copay = (form.data['desired_copay']) / (4500.0)
            coinsurance = (form.data['desired_in_network_coinsurance'] ) / ( 100.0 )
            deductible = (form.data['desired_in_network_deductible'] ) / 950.0
            moop =       (form.data['desired_in_network_out_of_pocket_maximum'] ) / ( 975.0 )
            visits =     (form.data['visits'] - 1) / ( 250 - 1)

            frame = dbf.soft_filters(frame, "health_insurance.db", form.data['age'], form.data['do_you_smoke'], form.data['benefits'],
                                     premium, coinsurance, copay, deductible, moop, visits, form.data['out_of_country'])

            # this is how we will get the list inputs

            # print( "Benefits:  " + str( form.cleaned_data['benefits'] ) )
            # print( "Benefits Type:  " + str( type( form.cleaned_data['benefits'])) + "\n")
            # print( "Diseases:  " + str( form.cleaned_data['diseases']))
            # print( "Diseases Type:  " + str( type(form.cleaned_data['diseases'])) + "\n")


            # resultsList = []
            # results = dbf.get_plan_information("health_insurance.db", frame)
            # res = results['Issuer_Name'].tolist()
            # for thing in res:
            #     object = BasicHealthInsuranceInfo()
            #     object.plan_name = thing
            #     resultsList.append(object)

            return render(request, 'results.html', {'resultsList': resultsList})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = HealthInsuranceInputForm()

    return render(request, 'index.html', {'form': form})

