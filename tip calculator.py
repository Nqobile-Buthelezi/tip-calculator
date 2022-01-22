print("Welcome diner, to my handy tip calculator.")

total_bill = float(input("What was the total bill?\nZAR"))

tip = float(input("How much of a tip would you like to give? 10, 12, or 15 percent?\n"))

total_diners = float(input("How many people to split the bill?\n"))

bill_plus_tip = total_bill * ((tip / 100) + 1)

each_diners_bill = bill_plus_tip / total_diners

bill_per_person = "{:.2f}".format(each_diners_bill)

print(f"Each person should pay: ZAR{bill_per_person}")