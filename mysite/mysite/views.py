import sys
import os
import pandas as pd
sys.path.append('..')
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.http import HttpResponseRedirect

from .forms import HealthInsuranceInputForm
from .forms import RecommendedHealthInsurances
# sys.path.append("/home/jesse/PycharmProjects/DDDM/mysite/database")
sys.path.insert(0, os.path.join( os.getcwd(), "mysite" ,"database") )
os.chdir( os.path.join( "database"))
import databasefunctions as dbf


# Create your views here.
def input(request):
    if request.method == 'POST':
        form = HealthInsuranceInputForm(request.POST)
        # print(form.zipcode)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            if form.data['months_tobacco_free']:
                frame = dbf.hard_filters_pg1("health_insurance.db", form.data['zipcode'], form.data['age'], 'Yes')
            else:
                frame = dbf.hard_filters_pg1("health_insurance.db", form.data['zipcode'], form.data['age'], 'No')
            # redirect to a new URL:

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


os.chdir(os.path.join(".."))