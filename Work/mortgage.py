# mortgage.py
#
# Exercise 1.7

principal = 500000.0
interest_rate = 0.05
monthly_payment = 2684.11
total_paid = 0.0

while principal > 0:
    principal = principal * (1+interest_rate/12) - monthly_payment
    total_paid = total_paid + monthly_payment

print('Total paid:', round(total_paid, ndigits=2))
