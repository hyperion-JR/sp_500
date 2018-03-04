
import datetime
import pandas as pd
import requests
from bs4 import BeautifulSoup

def change_func(neg_change, pos_change):
    if neg_change == None:
        change = pos_change
    else:
        change = neg_change
    return change.get_text()

def scrape_cnn_money(conn):
    data = {}
    url = 'http://money.cnn.com/data/markets/sandp/?page={}'
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
    conn.commit()
    print('Done loading data from CNN Money!')
    return df

def company_names(c, conn):
    data = {}
    cursor = c.execute('''SELECT DISTINCT * FROM sp''')
    for i in cursor:
        stock_name = i[0]
        co = i[2].replace(u'\xa0', u' ')
        co_name = co.split(' ', 1)[1]
        if stock_name not in data:
            data[stock_name] = pd.Series([co_name], index=['Name'])
    df = pd.DataFrame(data).T
    df.to_sql('sp', conn, if_exists='replace')
    conn.commit()
    print('Done loading companies data!')
    return df