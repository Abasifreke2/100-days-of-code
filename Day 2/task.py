print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
percentage = bill + (bill * tip/100)
final_payment = percentage/people
final_amount = round(final_payment, 2)
print(f"Each person is to pay {final_amount}" )

