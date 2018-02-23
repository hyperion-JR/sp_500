
import sqlite3
import requests
import pandas as pd
import numpy as np

from config import alpha_key

requests.session()
conn = sqlite3.connect('data.db')
c = conn.cursor()

def create_stocks_table():
    c.executescript('''DROP TABLE IF EXISTS stocks;''')
    c.execute('''CREATE TABLE stocks (stock, price_date, open, high, low, close, volume)''')
    conn.commit()
    print('Done creating stocks table.')

def list_of_sp_companies():
    sp_list = []
    cursor = c.execute('''SELECT DISTINCT stock FROM sp''')
    for i in cursor:
        stock = i[0]
        sp_list.append(stock)
    return sp_list

def load_stock_data():
    sp_list = list_of_sp_companies()
    for company in sp_list:
        print('Loading company: {}'.format(company))
        r = requests.get('https://www.alphavantage.co/query?outputsize=full&function=TIME_SERIES_DAILY&symbol=%s&interval=1min&apikey=%s' % (company, alpha_key['a_key']))
        r = r.json()
        for i in r['Time Series (Daily)']:
            dt = i
            opn = r['Time Series (Daily)'][i]['1. open']
            high = r['Time Series (Daily)'][i]['2. high']
            low = r['Time Series (Daily)'][i]['3. low']
            close = r['Time Series (Daily)'][i]['4. close']
            volume = r['Time Series (Daily)'][i]['5. volume']
            # Insert a row of data
            c.execute("INSERT INTO stocks VALUES (?,?,?,?,?,?,?)", (company,dt,opn,high,low,close,volume))
        conn.commit()
        print('Done loading {}'.format(company))

# Tests
# create_stocks_table()
# load_stock_data()
# conn.close()




