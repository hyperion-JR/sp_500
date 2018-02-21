
import datetime
import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'http://money.cnn.com/data/markets/sandp/?page={}'

def change_func(neg_change, pos_change):
    if neg_change == None:
        change = pos_change
    else:
        change = neg_change
    return change.get_text()

def get_data():
    data = {}
    for i in range(1, 34):
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
                if symbol not in data:
                    data[symbol] = pd.Series([co, price, change, dt], index=['Company','Price','Change','DatePulled'])
    return pd.DataFrame(data).T

def export_to_excel(data, file_name):
    writer = pd.ExcelWriter("%s.xlsx" % (file_name,))
    data.to_excel(writer,"%s" % (file_name,))
    writer.save()
    print('Done')

# To run, uncomment the code below
# export_to_excel(get_data(), 'SP Data')