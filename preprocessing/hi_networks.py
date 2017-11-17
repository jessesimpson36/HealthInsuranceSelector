import google
import csv
import newspaper
import pandas as pd
import json

json = json.load(open('issuerIDNames.json'))

with open('datasets/Hospitals.csv') as csvHospitals:
    csvReader = csv.reader(csvHospitals,delimiter='\t')
    for row in csvReader:
        hospital_id =row[2]
        hospital_name = row[4]
        hospital_state = row[8]
        hospital_status = row[13]
        print("*")

        if hospital_status == 'OPEN':
            search_results = google.search(hospital_name + " health insurance plans accepted", stop=5, lang="en")
            insurance_list_for_hospital = []
            for link in search_results:
                try:
                    data = newspaper.Article(url=link)
                    data.download()
                    data.parse()    w
                    text = data.text
                except:
                    continue

                for key in json:
                    name = key["name"]
                    split_name = name.split(" ")
                    length = len(split_name)
                    for i in range(length, 0, -1):
                        if (" ".join(split_name[0:i]) in text) and (hospital_state == key["state"]) :
                            insurance_list_for_hospital.append(key)
                            print(key)
                            break








