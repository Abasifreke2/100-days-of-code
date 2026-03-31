#The issue here was to resolve any possible error due to wrong value
#Like the user entering 'twelve' instead of '12'
try:
    age = int(input("How old are you?"))
except ValueError:
    print("You entered a non numerical response")
    age = int(input("How old are you?"))

if age > 18:
    print(f"You can drive at age {age}.")
