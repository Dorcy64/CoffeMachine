
from menu import MENU
from menu import resources


Water = resources["water"]
Milk = resources["milk"]
Coffee = resources["coffee"]
Income = 0

while 1 > 0:
    choice = input("What would you like? espresso/latte/cappuccino) : ")
    def coin_check():
        print("Please Insert Coins")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
        total = round(total, 2)
        return total

    def not_enough(waterq, milkq, coffeeq):
        if Water <= waterq:
            print("Sorry there is not enough water")
        elif Milk <= milkq:
            print("Sorry there is not enough milk")
        elif Coffee <= coffeeq:
            print("Sorry there is not enough cofee")

    def choicefunction(func_choice):
        global Income
        global Water
        global Coffee
        global Milk


        input_name = func_choice
        order_cost = MENU[input_name]["cost"]
        total_input = coin_check()
        if total_input >= order_cost:
            print(f"Here is ${total_input - order_cost} in change.")
            Income += order_cost

            Water -= MENU[input_name]["ingredients"]["water"]
            Coffee -= MENU[input_name]["ingredients"]["coffee"]
            Milk -= MENU[input_name]["ingredients"]["milk"]

            return f"Here is you {input_name} ☕ Enjoy!"
        else:
            return "Sorry that's not enough money. Money refunded."

    if choice == "report":
        print(f"Water = {Water}ml \nMilk = {Milk}ml \nCofee = {Coffee}g \nMoney: ${Income}")

    elif (choice == "espresso" or choice == "latte" or choice == "cappuccino") and Water >= 0 and Milk >= 0 and Coffee >= 0:
        if choice == "latte" and (Water < 200 or Milk < 150 or Coffee < 24):
            not_enough(200, 150, 24)
        elif choice == "espresso" and (Water < 50 or Milk < 0 or Coffee < 18):
            not_enough(50, 0, 18)
        elif choice == "cappuccino" and (Water < 250 or Milk < 100 or Coffee < 24):
            not_enough(250, 100, 24)
        elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
            print(choicefunction(choice))
    else:
        print("Inval1id input, choose from the 3 options bellow")