
income = float(input("what is your income: "))

if income <= 2820000:
    print("you have no tax")
elif 2820000 < income <= 4020000:
    new_income = (income - (income*0.9))
    print("your tax amount to be paid is", new_income)
elif 4020000 < income <= 4820000:
    tax_amount = (income-(income*0.8) + 120000)
    print("you will pay amount", tax_amount, "for your tax")
elif 4920000 < income >= 120000000:
    tax_amount = (income-((income*0.7) + 300000))
    print("tax_amount")
else:
    income > 120000000
    tax_amount = (income-((income*0.7) + 0.9 + 300000))
    print("you are rich to be paying", tax_amount, "as your tax")

