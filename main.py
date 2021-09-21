MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 100,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 150,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0

def is_resourse_sufficient(order_ingridients):
    # returns true when order can be made and false if ingredients are in sufficient
    is_enough = True
    for item in order_ingridients:
        if order_ingridients[item] > resources[item]:
            print(f"Sorry we do not have enough {item}.")
            is_enough = False
    return is_enough

def process_coins():
    # returns total calculated coins
    print("please insert coins.")
    total = int(input("how many One rupee coin "))*1
    total += int(input("how many Two rupee coin "))*2
    total += int(input("how many Five rupee coin "))*5
    total += int(input("how many Ten rupee coin "))*10
    return total

def is_transaction_successful(money_recieved , drink_cost):
#     return true when payment is accepted or false when money is insufficient
    if money_recieved >= drink_cost:
        change = round(money_recieved-drink_cost, 2)
        print(f"here's ${change} in change")
        #write globle before profit as profit outside
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
#     decuct the required ingredients from resources
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")
is_on = True
while is_on == True:
    choice = input(" What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on= False
    elif choice== "report":
        print(f"Water:{resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: {profit}")
    else:
        drink = MENU[choice]
        if is_resourse_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])







