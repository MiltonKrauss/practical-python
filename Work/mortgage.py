# mortgage.py
#
# Exercise 1.7

principal = 500000.0
interest_rate = 0.05
monthly_payment = 2684.11
total_paid = 0.0
month_number = 0

while month_number < 12:
    principal = principal * (1+interest_rate/12) - (monthly_payment + 1000)
    total_paid = total_paid + (monthly_payment + 1000)
    month_number = month_number + 1

while principal > 0:
    principal = principal * (1+interest_rate/12) - monthly_payment
    total_paid = total_paid + monthly_payment
    month_number = month_number + 1

print(f'Total paid: {total_paid:.2f}!')
print('Total number of months:', month_number)
