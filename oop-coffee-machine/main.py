from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu= Menu()



is_on= True
while is_on:
    user_input = input(f"What would you like to have? {menu.get_items()}")
    if user_input =="report":
        print(coffee_maker.report())
        print(money_machine.report())
        is_on=False
    elif user_input=="off":
        print("Machine Turning off")
        is_on=False
    else:
        drink = menu.find_drink(user_input)
        if drink!=None:
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)