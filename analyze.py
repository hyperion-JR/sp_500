
import sqlite3
import datetime
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from scipy import stats

scaler = StandardScaler()
conn = sqlite3.connect('data.db')
c = conn.cursor()

def create_sp_arrays():
    data = {}
    cursor = c.execute('''SELECT * FROM stocks''')
    for row in cursor:
        stock = row[0]
        price_date = datetime.datetime.strptime(row[1], '%Y-%M-%d').date()
        opn = float(row[2])
        high = float(row[3])
        low = float(row[4])
        close = float(row[5])
        change = close - opn
        volume = int(row[6])
        if stock not in data:
            data[stock] = []
        data[stock].append(change)
    return data

def sp_pop():
    # Deletes companies from dict that have less than 500 observations
    sp_dict = create_sp_arrays()
    new_sp_dict = {}
    del_sp_dict = {}
    for i, k in sp_dict.items():
        if len(k) >= 500:
            new_sp_dict[i] = k
        else:
            del_sp_dict[i] = k
    return new_sp_dict, del_sp_dict

def get_correlations():
    # Returns pearson correlation coefficient and p-value as it iterates through pairs of stocks
    sp_dict, del_sp_dict = sp_pop()
    correlations = {}
    list_of_companies = []
    dataframes = []
    for i, company in enumerate(sp_dict):
        list_of_companies.append(company)
    for i, k in enumerate(list_of_companies):
        if i < len(list_of_companies)-1:
            df = run_correlations(list_of_companies[i], sp_dict, list_of_companies)
            dataframes.append(df)
        else:
            continue
    return pd.concat(dataframes)

def run_correlations(y_company, sp_dict, list_of_companies):
    data = {}
    for i in list_of_companies:
        if i != y_company:
            x = scaler.fit_transform(np.array(sp_dict[i][:500]).reshape(-1,1))
            y = scaler.fit_transform(np.array(sp_dict[y_company][:500]).reshape(-1,1))
            pcc, p_value = stats.pearsonr(x, y)
            if i not in data:
                data[i] = pd.Series([y_company, i, pcc[0], p_value[0]], index=['Company Y','Company X', 'PCC', 'P-Value'])
    return pd.DataFrame(data).T

df = get_correlations()
sorted_df = df.sort_values(by=['PCC', 'P-Value'])
print(sorted_df)

    