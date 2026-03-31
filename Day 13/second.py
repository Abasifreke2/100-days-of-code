year = int(input("What's your year of birth?"))
#The code just omitted 1994
# if a user entered 1994 it would print nothing because there was no condition for that
if year > 1980 and year <= 1994:
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")
