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

print(os.getcwd())
pl = pd.read_csv("../../preprocessing/datasets/IssuerID_Name.csv")
plansList = pl['Issuer_Name'].tolist()
plans = [name + ' health insurance reviews' for name in plansList]

for p in plans:
    search_results = google.search(p, stop=4, lang="en")
    # print(search_results)
    print("*"*30)
    print(p.upper())
    print("_"*15)
    for link in search_results:
        # Beware of 403 errors. Still havent found a fix.i
        print(link)
        try:
            data = newspaper.Article(url=link)
            data.download()
            data.parse()
        except:
            continue

        text = data.text
        linesOfText = text.split('\n')
        for line in linesOfText:
            if( "found the following review helpful." in line):
                filtered = re.sub("[0-9]+ of [0-9]+ people found the following review helpful.", "", line)
                filtered = filtered.replace("Help others find the most helpful reviews Was this review helpful to you? Yes | No", "")
                print(filtered + '\n')
