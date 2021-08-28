

# data :

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
    "gain": 0
}


logo = """

    (  )   (   )  )
     ) (   )  (  (
     ( )  (    ) )
     _____________
    <_____________> ___
    |             |/ _ \
    |               | | |
    |               |_| |
 ___|             |\___/
/    \___________/    \
\_____________________/

"""


# coffee_machine functions :

menu_choice_list = []

for drink_name in MENU:
    menu_choice_list.append(drink_name)


espresso_choice = [MENU["espresso"]["ingredients"]["water"],
                   MENU["espresso"]["ingredients"]["coffee"],
                   MENU["espresso"]["cost"]]
print("espresso_details : ", espresso_choice)

latte_choice = [MENU["latte"]["ingredients"]["water"],
                MENU["latte"]["ingredients"]["milk"],
                MENU["latte"]["ingredients"]["coffee"],
                MENU["latte"]["cost"]]
print("latte_details : ",latte_choice)

cappuccino_choice = [MENU["cappuccino"]["ingredients"]["water"],
                     MENU["cappuccino"]["ingredients"]["milk"],
                     MENU["cappuccino"]["ingredients"]["coffee"],
                     MENU["cappuccino"]["cost"]]
print("capuccino_details : ",cappuccino_choice)

choice_list = [espresso_choice,
               latte_choice,
               cappuccino_choice]

choice_1 = choice_list[0]
choice_2 = choice_list[1]
choice_3 = choice_list[2]


def qantity_report_checker(description):

    if resources["water"] < 250 or resources["milk"] < 150 or resources["coffee"] < 24:
        print(f"Sorry not enough {description} ingredients to make it !! sold critic !!")
        print(f"Water : {resources['water']} ml, milk : {resources['milk']} ml, Coffee : {resources['coffee']} g, gain : $ {resources['gain']}")
        print("money refund!!")
        return False

    elif resources["water"] >= 250 or resources["milk"] >= 150 or resources["coffee"] >= 24:
        print(f"Water : {resources['water']} ml, milk : {resources['milk']} ml, Coffee : {resources['coffee']} g, gain : $ {resources['gain']}")
        return True

def use_purchasedDrink_ingredient(description):

    if description == "espresso":
        resources["water"] -= espresso_choice[0]
        resources["coffee"] -= espresso_choice[1]
        resources["gain"] += espresso_choice[-1]


    elif description == "latte":
        resources["water"] -= latte_choice[0]
        resources["milk"] -= latte_choice[1]
        resources["coffee"] -= latte_choice[2]
        resources["gain"] += latte_choice[-1]

    elif description == "cappuccino":
        resources["water"] -= cappuccino_choice[0]
        resources["milk"] -= cappuccino_choice[1]
        resources["coffee"] -= cappuccino_choice[2]
        resources["gain"] += cappuccino_choice[-1]

    return resources['water'],resources['milk'],resources['coffee'],resources['gain']

def process_coins(quarters,dimes,nickles,pennies):
    quarters_value = 0.25
    dimes_values = 0.10
    nickles_values = 0.05
    pennies_values = 0.01
    total_coins_inserted = float(quarters_value * quarters) + float(dimes_values * dimes) + float(nickles_values *nickles) + float(pennies_values * pennies)
    return total_coins_inserted

def transaction_checker(description_drink,drink_cost,coins_inserted):

    money_required = drink_cost - coins_inserted

    if money_required == 0:
        print(f"thanks, here is your {description_drink} Enjoy !! ")

    elif money_required < 0:
        money_required = round(-money_required, 2)
        print(f"You've insert too much money, here the change {money_required} $")
        print(f"Here is your {description_drink} Enjoy !")


    elif money_required > 0:
        money_required = round(money_required, 2)
        print(f"There isn't enough money for your drink,{money_required} left to pay, money refund !!")
        return False
#-------------------------------------------------------------------------------------

def coffee_machine():



    suggest_drink = int(input("What would you like? (☕︎ espresso : 1️⃣ /🧋latte : 2️⃣ /🥤cappuccino : 3️⃣ ) "))

    if qantity_report_checker(menu_choice_list[suggest_drink-1]) == False:
        return False

    else:

        if suggest_drink == 1:

            print("Please insert coins")
            nb_quarters = int(input("How many quarters ? : "))
            nb_dimes = int(input("How many dimes ? : "))
            nb_nickles = int(input("How many nickles ? : "))
            nb_pennies = int(input("How many pennies ? : "))

            process_coins(nb_quarters,nb_dimes,nb_nickles,nb_pennies)

            transaction_checker(menu_choice_list[0],
                                espresso_choice[-1],
                                process_coins(nb_quarters,nb_dimes,nb_nickles,nb_pennies))

            use_purchasedDrink_ingredient(menu_choice_list[0])



        elif suggest_drink == 2:


            print("Please insert coins")
            nb_quarters = int(input("How many quarters ? : "))
            nb_dimes = int(input("How many dimes ? : "))
            nb_nickles = int(input("How many nickles ? : "))
            nb_pennies = int(input("How many pennies ? : "))

            process_coins(nb_quarters,nb_dimes,nb_nickles,nb_pennies)

            transaction_checker(menu_choice_list[1],
                                latte_choice[-1],
                                process_coins(nb_quarters,nb_dimes,nb_nickles,nb_pennies))

            use_purchasedDrink_ingredient(menu_choice_list[1])

        elif suggest_drink == 3:

            print("Please insert coins")
            nb_quarters = int(input("How many quarters ? : "))
            nb_dimes = int(input("How many dimes ? : "))
            nb_nickles = int(input("How many nickles ? : "))
            nb_pennies = int(input("How many pennies ? : "))

            process_coins(nb_quarters, nb_dimes, nb_nickles, nb_pennies)

            transaction_checker(menu_choice_list[2],
                                cappuccino_choice[-1],
                                process_coins(nb_quarters, nb_dimes, nb_nickles, nb_pennies))

            use_purchasedDrink_ingredient(menu_choice_list[2])

def distribution():
    on = True
    while on:
        turn_on_coffee_machine = input("Would you like a drink ? Y / N ").lower()

        if turn_on_coffee_machine == "y":
            coffee_machine()


        elif turn_on_coffee_machine == "n":
            turn_off_coffee_machine = input("Would you like turn off the coffee_machine ? Y / N ").lower()
            if turn_off_coffee_machine == "y":
                print("OFF")
                on = False


            else:
                print("See you")


        elif turn_on_coffee_machine == "report":
            print(resources)
            
