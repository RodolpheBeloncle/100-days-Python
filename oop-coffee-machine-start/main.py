import coffee_maker
import menu
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Data

MyCoffeeMachine = CoffeeMaker()

Latte_Item = MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5)
Espresso_Item = MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5)
Cappuccino_Item = MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3)

MenuList = Menu()
MenuList.menu = [Latte_Item,Espresso_Item,Cappuccino_Item]

MyCashMachine = MoneyMachine()

on = True
#------------- End Data Coffee Machine --------------
while on:
    while True:
        MyCashMachine.report()
        MyCoffeeMachine.report()

        id = 0
        choice_list = {"1": "latte","2":"espresso","3": "cappuccino"}

        for choice in MenuList.menu:

            id += 1
            print(f"Choice {id} : {choice.name}, Cost : {choice.cost},Water : {choice.ingredients['water']},milk : {choice.ingredients['milk']}, Coffee: {choice.ingredients['coffee']}")


#--------------------------------------------

        suggest_drink = int(input("What would you like? : 🧋latte : 1️⃣ / ☕︎ espresso : 2️⃣ /🥤cappuccino : 3️⃣ => press a number "))

        MenuList.find_drink(MenuList.menu[suggest_drink - 1].name)

        if MyCoffeeMachine.is_resource_sufficient(MenuList.menu[suggest_drink - 1]) == False:
            on = False



        elif MyCashMachine.make_payment(MenuList.menu[suggest_drink - 1].cost) == False:
            break


        else:
            MyCoffeeMachine.make_coffee(MenuList.menu[suggest_drink - 1])


# ----- angela's solution ------

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        is_enough_ingredients = coffee_maker.is_resource_sufficient(drink)
        is_payment_successful = money_machine.make_payment(drink.cost)
        if is_enough_ingredients and is_payment_successful:
            coffee_maker.make_coffee(drink)


