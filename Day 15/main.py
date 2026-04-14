MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

def print_report():
    print(f"Water: {resources["water"]}")
    print(f"Milk: {resources["milk"]}")
    print(f"Coffee: {resources["coffee"]}")
    print(f"Money: {resources["money"]}")

def check_resources(drink):
    ingredients = MENU[drink]["ingredients"]
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True
def process_coins():
    print("Please insert your coins")
    quarters = int(input("How many quarters?")) * 0.25
    dimes = int(input("How many dimes?")) * 0.10
    nickles = int(input("How many nickles")) * 0.05
    pennies = int(input("How many pennies?")) * 0.01
    return round(quarters + dimes + nickles + pennies)

def check_transaction(coins, drink):
    cost = MENU[drink]["cost"]
    if coins < cost:
        print("Sorry that's not enough money. Money refunded")
        return False
    elif coins < cost:
        change = round(coins - cost,2)
        print(f"Here is {change} as change")
    resources["money"] += cost
    return True

def make_coffee(drink):
    ingredients = MENU[drink]["ingredients"]
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink}")

def menu():
    print(f"Espresso: {MENU["espresso"]["cost"]}")
    print(f"Latte: {MENU["latte"]["cost"]}")
    print(f"Cappuccino: {MENU["cappuccino"]["cost"]}")
machine_on = True

while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino) \n "
                   "You can also perform other functions like:\n"
                   "off: Turns off the machine\n"
                   "menu: Displays the  available coffee and their price\n"
                   "report: Displays available resources ").lower()
    if choice == "off":
        print("Okay turning off the machine")
        machine_on = False
    elif choice == "report":
        print_report()
    elif choice == "menu":
        menu()
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        if check_resources(choice):
            coins = process_coins()
            if check_transaction(coins, choice):
                make_coffee(choice)
    else:
        print("Invalid choice.")