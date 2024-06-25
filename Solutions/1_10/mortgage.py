# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

while principal > 0:
    interest = principal * (rate/12)
    if principal + interest < payment:
        payment = principal + interest #to adjust the extra payment
    prncp_payment = payment - interest
    principal = principal - prncp_payment
    total_paid = total_paid + payment
    month = month + 1
    print(month, round(total_paid,2), round(principal,2), round(interest,2))
    
print('Total paid', round(total_paid, 2))
print('Months', month)



