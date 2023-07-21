# pcost.py
#
# Exercise 1.27

import csv

def portfolio_cost(filename):
    'Determines total cost of portfolio'
    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            try:
                shares = int(row[1])
                price = float(row[2])
                cost = shares * price
                total_cost += shares * price
            except ValueError:
                print('Bad row:', row)
    return total_cost

import sys
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input('Enter a filename: ')
    
cost = portfolio_cost(filename)            
print('Total cost:', total_cost)
