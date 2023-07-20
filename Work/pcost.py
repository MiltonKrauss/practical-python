# pcost.py
#
# Exercise 1.27

with open('Data/portfolio.csv', 'rt') as file:
    headers = next(file)
    total_cost = 0
    for line in file:
        row = line.split(',')
        shares = int(row[1])
        price = float(row[2])
        cost = shares * price
        total_cost = total_cost + cost
    print('Total cost:', total_cost)
