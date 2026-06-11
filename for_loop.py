'''expenses = [1200,1300,1500]
total_expense = 0
for expense in expenses:
    total_expense = total_expense + expense

print(total_expense)
'''


montly_sales = [42, 38, 55, 67, 40, 45]
months = ["Jan","feb","mar","Apr","may","June"]
threshold = 63
for sales_amount, month in zip(montly_sales, months):
    #print(month,sales_amount)
    if sales_amount < threshold:
        print(f"sales amount {sales_amount} is less than the threshold in month {month}")
        #break
    else:
        print(f"sales amount {sales_amount} is greather than the threshold in month {month}")


