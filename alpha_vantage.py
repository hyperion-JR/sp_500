
import requests
import pandas as pd
import time

from config import alpha_key

def list_of_sp_companies(c):
    sp_list = []
    cursor = c.execute('''SELECT DISTINCT * FROM sp''')
    for i in cursor:
        stock = i[0]
        sp_list.append(stock)
    return sp_list

def load_stock_data(c, conn):
    sp_list = list_of_sp_companies(c)
    for company in sp_list:
        time.sleep(1.5)
        print('Loading company: {}'.format(company))
        r = requests.get('https://www.alphavantage.co/query?outputsize=full&function=TIME_SERIES_DAILY&symbol=%s&interval=1min&apikey=%s' % (company, alpha_key['a_key']))
        r = r.json()
        if r['Time Series (Daily)'] is None:
            continue
        result = r['Time Series (Daily)']
        for i in result:
            dt = i
            opn = result[i]['1. open']
            high = result[i]['2. high']
            low = result[i]['3. low']
            close = result[i]['4. close']
            volume = result[i]['5. volume']
            # Insert a row of data
            c.execute("INSERT INTO stocks VALUES (?,?,?,?,?,?,?)", (company,dt,opn,high,low,close,volume))
    conn.commit()
    print('Done loading {}'.format(company))