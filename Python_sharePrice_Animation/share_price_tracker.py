import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime

def real_time_price(stock_code):
    url = (('https://finance.yahoo.com/quote/') + stock_code + ('.HK?p=') + stock_code +  ('.HK&.trsc=fin-srch'))
    result = requests.get(url)

    web_content = BeautifulSoup(result.text,'lxml')
    web_content = web_content.find("div",{"class":'My(6px) Pos(r) smartphone_Mt(6px)'})

    if web_content == []:
        web_content = '9999'
    web_content = web_content.find('span').text
    return web_content


HSI = ['0001','0002','0003','0005']

for step in range(1,101):
    price = []
    col = []
    time_stamp = datetime.datetime.now()
    time_stamp = time_stamp.strftime('%Y-%m-%d %H:%M:%S')
    for stock_code in HSI:
        price.append(real_time_price(stock_code))
    col = [time_stamp]
    col.extend(price)
    df  = pd.DataFrame(col)
    df = df.T
    df.to_csv('real_time_stock_data.csv',mode = 'a',header = False)

