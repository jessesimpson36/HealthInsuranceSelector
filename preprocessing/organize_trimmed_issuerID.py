import csv
import json

issuerCSVFileName = "datasets/IssuerID_Name_Updated_Trimmed_Updated.csv"
plans = list()

with open(issuerCSVFileName) as hiPlansData:

    csvReader = csv.reader(hiPlansData, delimiter=',')

    for row in csvReader:

        # print(row)

        id = row[0]
        name = row[1]
        state = row[2]

        plan = dict()
        plan['id'] = id
        plan['name'] = name
        plan['state'] = state

        plans.append(plan)

# print(plans)
with open('issuerIDNames.json', 'w') as hiPlansOut:
    json.dump(plans, hiPlansOut)


