# mortgage.py
#
# Exercise 1.7

principal = 500000.0
interest_rate = 0.05
monthly_payment = 2684.11
total_paid = 0.0
month_number = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    
    while month_number >= extra_payment_start_month and month_number <= extra_payment_end_month:
        principal = round(principal * (1+interest_rate/12) - (monthly_payment + extra_payment), 2)
        total_paid = round(total_paid + (monthly_payment + extra_payment), 2)
        month_number = month_number + 1
        print(month_number, total_paid, principal)
    principal = round(principal * (1+interest_rate/12) - monthly_payment, 2)
    total_paid = round(total_paid + monthly_payment, 2)
    month_number = month_number + 1
    print(month_number, total_paid, principal)

    if principal < monthly_payment:
        monthly_payment = principal * (1+interest_rate/12)

print(f'Total paid: {total_paid:.2f}!')
print('Total number of months:', month_number)
