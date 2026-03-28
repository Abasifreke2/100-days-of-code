import art
print(art.logo)

def add(n1, n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1/n2
operator = {
    "+": add,
    "-": subtract,
    "*":multiply,
    "/":divide
}
first_loop = True
while first_loop:
    first_number = float(input("What is your first number: "))
    Loop = True
    while Loop:
        operation = input("\n+\n-\n*\n/ \nWhat operation would you like to perform: ")
        second_number = float(input("What is your second number: "))
        calculate = operator[operation](n1=first_number,n2=second_number)
        print(f"Your answer is {calculate}")
        Should_continue = input(f"Type 'y' to continue calculating with {calculate} and type 'n' to start a new calculation").lower()
        if Should_continue == "y":
            first_number = calculate
        if Should_continue == "n":
            Loop = False
