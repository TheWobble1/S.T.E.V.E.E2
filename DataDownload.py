from numpy.ma.core import count
from yahoo_fin import stock_info
from datetime import datetime
from datetime import date
import csv

Stocks = ['GOOG', 'AAPL']

def File_Maker(Asset):
    data = [
        ['Date', 'Time', 'Price']
    ]
    Date = str(date.today())
    with open(Asset + Date + '.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

def Data_Fetch(Asset):
    Data = stock_info.get_live_price(Asset)
    return Data

def Data_Write(Asset):
    Price = Data_Fetch(Asset)
    Date = str(date.today())
    Time = datetime.now()
    Time = Time.strftime('%H:%M:%S')

    New_Data = [Date, Time, Price]
    with open(Asset + Date + '.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(New_Data)

# Startup Code
for i in range(count(Stocks)):
    File_Maker(Stocks[i])

# Main Code
Hour = 0   # If in UK value should be 14
Min = 17    # If in UK value should be 30
while True:
    Time = datetime.now()
    if Time.hour == Hour and Time.minute == Min:
        for i in range(count(Stocks)):
            Data_Write(Stocks[i])
        Min = Min + 1
        if Min > 60:
            Hour = Hour + 1
            Min = 0
        if Hour == 21:
            Hour = 14
            Min = 30