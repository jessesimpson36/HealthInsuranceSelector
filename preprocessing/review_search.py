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

# print(os.getcwd())
f = open( "output.csv" , 'w', encoding="latin")

pl = pd.read_csv("../../preprocessing/datasets/IssuerID_Name.csv")
plansList = pl['Issuer_Name'].tolist()
idList = pl['IssuerID'].tolist()
plans = [name + ' health insurance reviews' for name in plansList]

number_of_companies_reviewed = 0
total_companies = 0
indexInPlans = 0;

for p in plans:
    f.write(str( idList[indexInPlans] ) + ", ")
    indexInPlans += 1
    total_companies += 1

    search_results = google.search(p, stop=4, lang="en")
    print("*"*30)
    print(p.upper())
    print("_"*15)
    iterated = 0
    for link in search_results:
        if ( ("www.bbb.org" not in link) and ("usinsuranceagents.com" not in link)):
            continue
        try:
            data = newspaper.Article(url=link)
            data.download()
            data.parse()
        except:
            continue

        text = data.text
        linesOfText = text.split('\n')

        if( "usinsuranceagents.com" in link):
            for line in linesOfText:
                if( "found the following review helpful." in line):
                    if (iterated == 0):
                        number_of_companies_reviewed += 1
                        iterated = 1
                    filtered = re.sub("[0-9]+ of [0-9]+ people found the following review helpful.", "", line)
                    filtered = filtered.replace("Help others find the most helpful reviews Was this review helpful to you? Yes | No", "")
                    filtered = filtered.replace(",", " ")
                    filtered = filtered.replace("\n", " ")
                    # filtered.encode('ascii', errors='ignore')
                    f.write(filtered)
                    print(filtered + '\n')
            f.write("\n")
        # if ( "www.bbb.org" in link ):
        #     for line in linesOfText:
        #         filtered_stars = re.search("([0-9.]+) out of 5 stars", line)
        #         filtered_letter = re.search("a BBB Rating of ([A-Z+-]+)", line)
        #         if (filtered_stars is not None):
        #             if (iterated == 0):
        #                 number_of_companies_reviewed += 1
        #                 iterated = 1
        #             # CUSTOMER STAR RATING
        #             print(filtered_stars.group(1) + "    ")
        #
        #         if (filtered_letter is not None):
        #             if (iterated == 0):
        #                 number_of_companies_reviewed += 1
        #                 iterated = 1
        #             # LETTER RATING
        #             print(filtered_letter.group(1))
        #
        # print( "Number reviewed:   " + str( number_of_companies_reviewed) +  "   Total:    "  + str(total_companies) )


f.close()
