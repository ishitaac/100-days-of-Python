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
}

def enough_resources(drink_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in drink_ingredients:
        if drink_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True

def payment_process():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def payment_success(payment, cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if payment> cost:
        change = round(payment- cost, 2)
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink, drink_ingredients,):
    """Deduct the required ingredients from the resources."""
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print(f"Here is your {drink} ☕️. Enjoy!")


money = 0
choice = input("​What would you like? (espresso/latte/cappuccino): ").lower()

if choice == "report":
    print(f"Water : {resources['water']}ml" )
    print(f"Milk : {resources['milk']}ml" )
    print(f"Coffee : {resources['coffee']}ml" )
    print(f"Money: ${money}")

else:
    drink = MENU[choice]
    if enough_resources(drink["ingredients"]):
        pay = payment_process()
        if payment_success(pay, drink["cost"]):
            make_coffee(choice, drink["ingredients"] )
