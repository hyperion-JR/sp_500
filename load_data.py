
import sqlite3
import pandas as pd

from scrape_cnn_money import scrape_cnn_money
from alpha_vantage import load_stock_data

conn = sqlite3.connect('data.db')
c = conn.cursor()

def create_sp_table():
    c.executescript('''DROP TABLE IF EXISTS sp;''')
    c.execute('''CREATE TABLE sp (stock, company, price, change, scrape_date)''')
    conn.commit()
    print('Done creating sp table.')

def create_stocks_table():
    c.executescript('''DROP TABLE IF EXISTS stocks;''')
    c.execute('''CREATE TABLE stocks (stock, price_date, open, high, low, close, volume)''')
    conn.commit()
    print('Done creating stocks table.')

def export_to_excel(data, file_name):
    writer = pd.ExcelWriter("%s.xlsx" % (file_name,))
    data.to_excel(writer,"%s" % (file_name,))
    writer.save()
    print('Done')

if __name__ == '__main__':
    create_sp_table()
    scrape_cnn_money(conn)
    create_stocks_table()
    load_stock_data(c, conn)
    conn.close()


