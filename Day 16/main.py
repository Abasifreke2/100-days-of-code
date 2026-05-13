from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
machine_on  = True
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
while machine_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options} \n "
                       "You can also perform other functions like:\n"
                       "off: Turns off the machine\n"
                       "report: Displays available resources ").lower()
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        machine_on = False
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
