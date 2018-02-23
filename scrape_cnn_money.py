
import sqlite3
import datetime
import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'http://money.cnn.com/data/markets/sandp/?page={}'

conn = sqlite3.connect('data.db')
c = conn.cursor()

def create_sp_table():
    c.executescript('''DROP TABLE IF EXISTS sp;''')
    c.execute('''CREATE TABLE sp (stock, company, price, change, scrape_date)''')
    conn.commit()
    print('Done creating sp table.')

def change_func(neg_change, pos_change):
    if neg_change == None:
        change = pos_change
    else:
        change = neg_change
    return change.get_text()

def scrape_cnn_money():
    data = {}
    # Probably a better way to handle this part...
    for i in range(0, 35):
        r = requests.get(url.format(i))
        soup = BeautifulSoup(r.text, 'lxml')
        body = soup.find_all('tbody')
        for b in body:
            companies = b.find_all('tr')
            for c in companies:
                symbol = c.find(attrs={'class':'wsod_symbol'}).get_text()
                co = c.find('td').get_text()
                price = c.find('span').get_text()
                dt = datetime.datetime.today()
                neg_change = c.find(attrs={'class':'negData'})
                pos_change = c.find(attrs={'class':'posData'})
                change = change_func(neg_change, pos_change)
                print(symbol, co, price, change, dt)
                if symbol not in data:
                    data[symbol] = pd.Series([symbol, co, price, change, dt], index=['Stock', 'Company','Price','Change','DatePulled'])
    df = pd.DataFrame(data).T
    df.to_sql('sp', conn, if_exists='replace')
    return df

def export_to_excel(data, file_name):
    writer = pd.ExcelWriter("%s.xlsx" % (file_name,))
    data.to_excel(writer,"%s" % (file_name,))
    writer.save()
    print('Done')

# Tests
# create_sp_table()
# df = scrape_cnn_money()
# export_to_excel(df, 'SP')

