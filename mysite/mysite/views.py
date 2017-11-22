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
from .forms import RecommendedHealthInsurances
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
            frame = dbf.hard_filters_pg1("health_insurance.db", form.data['zipcode'], form.data['age'], form.data['do_you_smoke'])

            # redirect to a new URL:

            # this is how we will get the list inputs
            print( "Benefits:  " + str( form.cleaned_data['benefits'] ) )
            print( "Benefits Type:  " + str( type( form.cleaned_data['benefits'])) + "\n")
            print( "Diseases:  " + str( form.cleaned_data['diseases']))
            print( "Diseases Type:  " + str( type(form.cleaned_data['diseases'])) + "\n")


            resultsList = []
            results = dbf.get_plan_names("health_insurance.db", frame)
            res = results['Issuer_Name'].tolist()
            for thing in res:
                object = RecommendedHealthInsurances()
                object.plan_name = thing
                resultsList.append(object)

            return render(request, 'results.html', {'resultsList': resultsList})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = HealthInsuranceInputForm()

    return render(request, 'index.html', {'form': form})

