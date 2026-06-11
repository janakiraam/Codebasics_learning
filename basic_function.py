def expense(expenses):
    total = 0
    for expen in expenses:
        total = total + expen
    return total

expense_raam = [45,67,89,90]
expense_janaki = [67,89,56,43]

total_expense_raam = expense(expense_raam)
print("total expense raam", total_expense_raam)

