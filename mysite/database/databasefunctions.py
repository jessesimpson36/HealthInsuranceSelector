import sqlite3
import pandas as pd
import numpy as np
from scipy.spatial.distance import euclidean
import uszipcode

# -------------------- User Preferences
# State - NC
# Zipcode - 27606
# Age - 26
# Tobacco Usage - No
# Disease Management - Diabetes
# Coinsurance - 20% (0)
# Deductible IN - 200 (1)
# MOOP IN - 100 (0)

def get_benefits( db_loc ):
    # conn, c = create_connection( db_loc )
    conn, c = create_connection( "health_insurance.db" )
    results = c.execute("SELECT distinct benefit_name FROM benefits order by benefit_name")
    benefits = results.fetchall()
    benefits = [b[0] for b in benefits]
    ben = [(b,str(b).title()) for b in benefits]
    # benefits = pd.DataFrame(results.fetchall())
    # benefits.columns = [col[0] for col in results.description]
    close_connection( conn, c)
    return tuple(ben)

def create_connection(db_loc):
    conn = sqlite3.connect(db_loc)
    c = conn.cursor()
    return conn, c


def close_connection(conn, c):
    c.close()
    conn.close()


def hard_filters_pg1(db_loc, zip = None, age = None, tobacco_usage = None):
    if zip == None or str(zip).strip() == "" or age == None or str(age).strip() == "" or tobacco_usage == None:
        return "Enter all inputs"
    search = uszipcode.ZipcodeSearchEngine()
    state = None
    if str(zip).strip() != "":
        if search.by_zipcode(str(zip)):
            state = search.by_zipcode(str(zip))['State']
        else:
            return "Invalid zipcode"
    conn, c = create_connection(db_loc)
    if tobacco_usage == "Yes":
        results = c.execute("SELECT distinct plan_id, smoker_rate FROM cost where state = ? AND age_lower <= ? AND "
                            "age_higher >= ? ", (state, age, age))
    else:
        results = c.execute("SELECT distinct plan_id, indiv_rate FROM cost where state = ? AND age_lower <= ? AND "
                            "age_higher >= ? ", (state, age, age))

    if not results:
        print("No plans are available in your area covering your condition. Checking for closest match..")
        results = c.execute("SELECT * FROM PLAN_ATTRIBUTES where STATECODE = ?" , (state,))

    hard_df = pd.DataFrame(results.fetchall())
    print(results.description)
    hard_df.columns = [description[0] for description in results.description]
    close_connection(conn, c)
    return hard_df

def get_plan_names(db_loc, hard_df1):
    conn, c = create_connection(db_loc)
    res = list(set(hard_df1['plan_id'].apply(lambda x: x[0:5])))
    query = "SELECT * FROM IssuerID_Name_Mapping where IssuerID IN (" + ','.join(res) + ")"
    results = c.execute(query)
    names = pd.DataFrame(results.fetchall())
    names.columns = [col[0] for col in results.description]
    close_connection(conn, c)
    return names

if __name__ == "__main__":
    hard_filters_pg1()