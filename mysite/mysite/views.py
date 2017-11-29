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

            diseases = form.cleaned_data['diseases']
            benefits = form.cleaned_data['benefits']

            if diseases == []:
                diseases = None
            else:
                diseases = form.data['diseases']

            if benefits == []:
                benefits = None
            else:
                benefits = form.data['benefits']

            if form.data['desired_premium_price'] == "":
                desired_premium_price = 0
            else:
                desired_premium_price = int(form.cleaned_data['desired_premium_price'])

            # process the data in form.cleaned_data as required
            frame = dbf.hard_filters_pg1("health_insurance.db", form.data['zipcode'], form.data['age'], form.data['do_you_smoke'],
                                         diseases, benefits, desired_premium_price)
            if not isinstance(frame, pd.DataFrame):
                if frame is False:
                    print('Indicate on frontend no results were found for given inputs')
                    return render(request, 'index.html', {'form': form})
                elif frame == "Invalid entry":
                    print("Indicate on frontend inputs are invalid")
                    return render(request, 'index.html', {'form': form})
            if form.data['do_you_smoke'] == "Yes":
            # normalize inputs (premium, copay, coinsurance, deductible, moop, visits)
            # the values obtained were found using database maxes and mins
                if ( desired_premium_price == 0):
                    premium = 0
                else:
                    premium = (desired_premium_price - 73 ) / ( 2673.63 - 73 )

            else:
                if ( desired_premium_price == 0):
                    premium = 0
                else:
                    premium = (desired_premium_price - 73.0 )/ (2314.71 - 73)


            if form.data['desired_copay'] != "":
                copay = (int( form.data['desired_copay'])) / (4500.0)
            else:
                copay = 0

            if form.data['desired_in_network_coinsurance'] != "":
                coinsurance = (int( form.data['desired_in_network_coinsurance'] )) / ( 100.0 )
            else:
                coinsurance = 0

            if form.data['desired_in_network_deductible'] != "":
                deductible = (int( form.data['desired_in_network_deductible']) ) / 950.0
            else:
                deductible = 0

            if form.data['desired_in_network_out_of_pocket_maximum'] != "":
                moop =       ( int( form.data['desired_in_network_out_of_pocket_maximum'] )) / ( 975.0 )
            else:
                moop = 0

            if form.data['number_of_visits'] != "":
                visits =     (int( form.data['number_of_visits']) - 1) / ( 250 - 1)
            else:
                visits = 0

            out_of_country = .5
            if form.cleaned_data['out_of_country'] != '':
                out_of_country = form.cleaned_data['out_of_country']

            soft_frame = dbf.soft_filters(frame, "health_insurance.db", form.data['age'], form.data['do_you_smoke'], benefits,
                                     premium, coinsurance, copay, deductible, moop, visits, out_of_country)
            if not isinstance(soft_frame, pd.DataFrame) and soft_frame is False:
                print('Indicate on frontend no results were found for given inputs')
                return render(request, 'index.html', {'form': form})


            # this is how we will get the list inputs

            # print( "Benefits:  " + str( form.cleaned_data['benefits'] ) )
            # print( "Benefits Type:  " + str( type( form.cleaned_data['benefits'])) + "\n")
            # print( "Diseases:  " + str( form.cleaned_data['diseases']))
            # print( "Diseases Type:  " + str( type(form.cleaned_data['diseases'])) + "\n")

            print( soft_frame.columns)
            print( soft_frame.values.tolist() )


            resultsList = []
            for index, item in enumerate( soft_frame.itertuples()):
                temp = BasicHealthInsuranceInfo()
                temp.issuer_name = item[5]
                temp.plan_name = item[4]
                temp.premium_price = item[3]
                temp.issuer_id = item[6]
                temp.plan_id = item[1]
                temp.diseases = item[9]
                temp.moop = item[10]
                if item[7] == 1:
                    temp.out_of_country = "Covered"
                else:
                    temp.out_of_country = "Not Covered"

                temp.coinsurance = item[16]
                temp.copay = item[14]

                ratings, reviews, benefits, links = dbf.get_plan_information("health_insurance.db",
                                                                             temp.issuer_id,
                                                                             temp.plan_id)

                for x in ratings.itertuples():
                    temp.bbb_rating = x[1]
                    temp.customer_rating = x[2]
                    # print("Ranking " + temp.bbb_rating)
                    # print("CusRanking " + temp.customer_rating)
                for y in links.itertuples():
                    temp.enrollment_link = y[1]
                    temp.brochure_link = y[2]

                temp.benefits = benefits
                for z in reviews.itertuples():
                    temp.pos_count = z[1]
                    temp.neg_count = z[2]
                    temp.high_count = z[3]
                    temp.low_count = z[4]
                    print(z[1])
                    print(z[2])
                    print(z[3])
                    print(z[4])

                print(reviews)
                # print(benefits)
                # for z in benefits.itertuples():
                #     temp.benefits = z[1]
                #     print(z[1])

                resultsList.append(temp)
                # print( temp.premium_price)
                # print( temp.plan_name)
                # print( temp.issuer_id)
                # print( temp.plan_id)
                # print( temp.issuer_name + "\n")


            # results = dbf.get_plan_information("health_insurance.db", frame)
            # res = results['Issuer_Name'].tolist()
            # for thing in res:
            #     object = BasicHealthInsuranceInfo()
            #     object.plan_name = thing
            #     resultsList.append(object)

            # print( ratings )
            # print( reviews )
            # print( benefits )
            # print( links )
            # return render(request, 'index.html', {'form': form})
            return render(request, 'results.html', {'resultsList': resultsList})


    # if a GET (or any other method) we'll create a blank form
    else:
        form = HealthInsuranceInputForm()

    return render(request, 'index.html', {'form': form})

