# For this test I will use 2 screening tests
# Test A: 1% in an hour
# Test B: 0.5% in 5 min
# Test C: 0.1% in 1 min
from datetime import date
from numpy.ma.core import count
import csv

Stocks = ['GOOG', 'AAPL']

def Test_A(Asset):
    Date = str(date.today())

    with open(Asset + Date + '.csv', mode='r') as file:

        csv_reader = csv.reader(file)

        # Skip the header row (if there is one)
        next(csv_reader, None)

        # Iterate over each row in the CSV file
        for row in csv_reader:
            print(row['Price'])

        #def Test_B():
#def Test_C():

for i in range(count(Stocks)):
    Test_A(Stocks[i])