import newspaper
import google
import pandas as pd
import re
import time

pl = pd.read_csv("/home/jesse/PycharmProjects/DDDM/preprocessing/datasets/IssuerID_Name_Updated_Trimmed_Updated.csv")
issuers = pd.read_csv("/home/jesse/PycharmProjects/DDDM/preprocessing/datasets/Plan_Attributes_PP2.csv", usecols=[1])


issuer_ids = issuers['IssuerId'].tolist()
pl = pl[pl['IssuerID'].isin(issuer_ids)]
IssuerName = pl['Issuer_Name'].tolist()
idList = pl['IssuerID'].tolist()
stateList = pl['State'].tolist()

review_df = pd.DataFrame(data={'IssuerID': idList, 'IssuerName': IssuerName, 'State': stateList})
review_df.to_csv("/home/jesse/PycharmProjects/DDDM/preprocessing/167plans.csv", index=False)

