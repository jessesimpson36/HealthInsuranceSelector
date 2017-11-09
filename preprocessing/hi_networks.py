import google
import csv
import newspaper
import time

health_insurance_list = ["Humana", "Cigna", "BlueCross", "Aetna" ]

with open('datasets/Hospitals.csv') as csvHospitals:
    csvReader = csv.reader(csvHospitals,delimiter='\t')
    for row in csvReader:
        hospital_id =row[2]
        hospital_name = row[4]
        hospital_zip = row[9]
        hospital_status = row[13]

        if hospital_status == 'OPEN':
            search_results = google.search(hospital_name + " health insurance plans accepted", stop=5, lang="en")
            for link in search_results:
                data = newspaper.Article(url=link)
                data.download()
                data.parse()
                text = data.text

                for hi in health_insurance_list:
                    if hi in text:
                        print( hi )



