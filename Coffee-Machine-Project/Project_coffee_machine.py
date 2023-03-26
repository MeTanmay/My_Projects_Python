from art import logo

MENU = {
    "Espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "Latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "Cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
print(logo)
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_resources(order_ingredients):
    
    for item in order_ingredients:
        if order_ingredients[item]>=resources[item]:
            print(f"Sorry there is no enough {item} .")
            return False
    return True


def process_coins():
    print("Please insert coins")
    quarter=int(input("how many quarters: "))
    dimes=int(input("how many dimes: "))
    nickels=int(input("how many nickels: "))
    pennies=int(input("how many pennies: "))
    total=quarter*0.25 + dimes*0.10 + nickels*0.05 + pennies*0.01
    return total
    
def is_transaction_success(money_recieved,drink_cost):    
    if money_recieved>=drink_cost:
        change=round(money_recieved-drink_cost,2)
        print(f"Here is {change}  in change")
        global profit 
        profit +=drink_cost
        return True
        
    else:
        print("Sorry Thats not enough money. Money refunded")
        return False

def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"Here is your {drink_name} ☕☕. Enjoy!!")
        

is_on=True
while is_on:
    choice=input("What would you like? (Espresso/ Latte/ Cappuccino) : ")
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f'Water: {resources["water"]} ml')
        print(f'Milk: {resources["milk"]} ml')
        print(f'Coffee: {resources["coffee"]}g') 
        print(f'Money: {profit}')
    else:
        drink=MENU[choice]
        if check_resources(drink["ingredients"]):
            payment=process_coins()
            if is_transaction_success(payment,drink["cost"]):
                make_coffee(choice,drink["ingredients"])


        
            
        
      
