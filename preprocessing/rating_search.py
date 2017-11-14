'''
    This code returns results that contains a figure
    for insurance plans with information about it
    retrieved from Google.
    A more refined version would include particular
    keywords from our truth table like deductible,
    copay, etc.
'''

import newspaper
import google
import re
import pandas as pd
import os
from fake_useragent import UserAgent
ua = UserAgent()
# print(os.getcwd())

pl = pd.read_csv("/home/jesse/PycharmProjects/DDDM/preprocessing/datasets/IssuerID_Name_Updated.csv")
issuers = pd.read_csv("/home/jesse/PycharmProjects/DDDM/preprocessing/datasets/Plan_Attributes_PP2.csv", usecols=[1])

customer_ranking = []
bbb_ranking = []

issuer_ids = issuers['IssuerId'].tolist()
pl = pl[pl['IssuerID'].isin(issuer_ids)]
plansList = pl['Issuer_Name'].tolist()
idList = pl['IssuerID'].tolist()
plans = [name + ' bbb.org health insurance reviews' for name in plansList]
comments = []

number_of_companies_reviewed = 0
total_companies = 0
indexInPlans = 0;

for p in plans:
    plan_comm = []

    indexInPlans += 1
    total_companies += 1

    search_results = google.search(p, stop=4, lang="en", user_agent=ua.random)
    print("*"*30)
    print(p.upper())
    print("_"*15)
    iterated = 0
    starFlag = True
    letterFlag = True

    # Goes through the first 10 links in the search results and finds information
    # within our 2 trusted sources
    for link in search_results:
        if ( ("www.bbb.org" not in link) ):
            continue
        try:
            data = newspaper.Article(url=link)
            data.download()
            data.parse()
        except:
            continue

        text = data.text
        linesOfText = text.split('\n')
        # print("Text complete: " + text)
        for line in linesOfText:
            filtered_stars = re.search("([0-9.]+) out of 5 stars", line)
            filtered_letter = re.search("a BBB Rating of ([A-Z+-]+)", line)
            if ( starFlag ):
                if (filtered_stars is not None):
                    if (iterated == 0):
                        number_of_companies_reviewed += 1
                        iterated = 1
                    # CUSTOMER STAR RATING
                    print(filtered_stars.group(1) + "    ")
                    customer_ranking.append(filtered_stars.group(1))
                    starFlag = False
                else:
                    customer_ranking.append("None")
                    starFlag = False

            if ( letterFlag ):
                if (filtered_letter is not None):
                    if (iterated == 0):
                        number_of_companies_reviewed += 1
                        iterated = 1
                    # LETTER RATING
                    print(filtered_letter.group(1))
                    bbb_ranking.append(filtered_letter.group(1))
                    letterFlag = False
                else:
                    bbb_ranking.append("None")
                    letterFlag = False

    # if there isn't any rankings found, we still need to write None to the csv
    if starFlag:
        customer_ranking.append("None")

    if letterFlag:
        bbb_ranking.append("None")

        # Prints out the number of companies reviewed and the total number of companies so we know
        # how many companies are being represented by our websites and filters.
        print( "Number reviewed:   " + str( number_of_companies_reviewed) +  "   Total:    "  + str(total_companies) )

# writes all of the customer and bbb rankings into a csv file
df = pd.DataFrame(data={'IssuerID':idList, 'CustomerRanking':customer_ranking  ,'BBBRanking':bbb_ranking})
df.to_csv("BBBRatings.csv", index=False)

