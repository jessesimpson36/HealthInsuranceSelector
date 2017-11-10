import sys
sys.path.append('..')

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.http import HttpResponseRedirect

from .forms import HealthInsuranceInputForm
from utils.example import functionEx


# Create your views here.
def input(request):
    if request.method == 'POST':
        form = HealthInsuranceInputForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

            functionEx(form.cleaned_data.get('age'), form.cleaned_data.get('zipcode'))

            return render(request, 'results.html', {'form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = HealthInsuranceInputForm()

    return render(request, 'index.html', {'form': form})

