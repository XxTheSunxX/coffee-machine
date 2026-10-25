import sys

# cash value
QUARTERS = 0.25 # value of quarters
PENNIES = 0.01 # value of pennies
NICKLES = 0.05 # value of nickles
DIMES = 0.10 # value of dimes

# resources
WATER = 1000 # GALLONS
COFFEE = 100 # GRAMS
MILK = 1000 # GALLONS

# cash collected by machine
MONEY = 0.0


def check_resources(option):
    """Check resources left inside the machine"""

    if option == 1:

        if WATER < 50:
            print("Not enough water. Please refill the machine's water tank.")
            return False
        if COFFEE < 18:
            print("Not enough coffee. Please refill the coffee tank.")
            return False
        return True

    if option == 2:

        if WATER < 200:
            print("Not enough water. Please refill the machine's water tank.")
            return False
        if COFFEE < 24:
            print("Not enough coffee. Please refill the coffee tank.")
            return False
        if MILK < 150:
            print("Not enough milk. Please refill the milk tank.")
            return False
        return True

    if option == 3:

        if WATER < 250:
            print("Not enough water. Please refill the machine's water tank.")
            return False
        if COFFEE < 24:
            print("Not enough coffee. Please refill the coffee tank.")
            return False
        if MILK < 100:
            print("Not enough milk. Please refill the milk tank.")
            return False
        return True


def process_money():
    """Process the money"""

    money = 0

    qrt = input("Quarters: ")
    qrt = float(qrt) * QUARTERS

    di = input("Dimes: ")
    di = float(di) * DIMES

    nic = input("Nickles: ")
    nic = float(nic) * NICKLES

    pen = input("Pennies: ")
    pen = float(pen) * PENNIES

    money = qrt + di + nic + pen
    return round(money, 2)


def deduct_resources(option):
    """Take the drink's ingredients out of the machine.
    Call this only after check_resources() passed and the money was accepted."""

    global WATER
    global COFFEE
    global MILK
 
    if option == 1:
        WATER = WATER - 50
        COFFEE = COFFEE - 18
 
    if option == 2:
        WATER = WATER - 200
        COFFEE = COFFEE - 24
        MILK = MILK - 150
 
    if option == 3:
        WATER = WATER - 250
        COFFEE = COFFEE - 24
        MILK = MILK - 100


def espresso():
    """Espresso option"""

    COST = 1.50
    CHANGE = 0
    global MONEY

    option = 1

    # if resource are available, continue
    if not check_resources(option):
        return

    # collect money
    print("Enter the appropriate amount of coins: $1.50 ")
    money = process_money()

    # check in resources is sufficient
    if money < COST:
        print(f"Not enough money. ${money:.2f} refunded.")
        return

    else:
        print("Processing Espresso now...")
        print("Whirl... Coffee is ready. Enjoy!")

    # calculate change
    deduct_resources(option)
    MONEY = MONEY + COST
    CHANGE = money - COST
    print(f"Please take your change: ${CHANGE:.2f}")
    return


def latte():
    """Latte option"""

    COST = 2.50
    CHANGE = 0
    global MONEY

    option = 2
    # if resource are available, continue
    if not check_resources(option):
        return

    # collect money
    print("Enter the appropriate amount of coins: $2.50 ")
    money = process_money()

    # check in resources is sufficient
    if money < COST:
        print(f"Not enough money. ${money:.2f} refunded.")
        return

    else:
        print("Processing Latte now...")
        print("Whirl... Coffee is ready. Enjoy!")

    # calculate change
    deduct_resources(option)
    MONEY = MONEY + COST
    CHANGE = money - COST
    print(f"Please take your change: ${CHANGE:.2f}")
    return


def cappuccino():
    """cappuccino option"""

    COST = 3.00
    CHANGE = 0
    global MONEY

    option = 3
    # if resource are available, continue
    if not check_resources(option):
        return

    # collect money
    print("Enter the appropriate amount of coins: $3.00 ")
    money = process_money()

    # check in resources is sufficient
    if money < COST:
        print(f"Not enough money. ${money:.2f} refunded.")
        return

    else:
        print("Processing Cappuccino now...")
        print("Whirl... Coffee is ready. Enjoy!")

    # calculate change
    deduct_resources(option)
    MONEY = MONEY + COST
    CHANGE = money - COST
    print(f"Please take your change: ${CHANGE:.2f}")
    return


def report():
    """Display's the report for the resources in the machine"""
    print(f"Money: ${MONEY:.2f}")
    print(f"Water: {WATER}")
    print(f"Coffee: {COFFEE}")
    print(f"Milk: {MILK}")


def main():
    """Main function where all other functionality is called"""
    print("Super Co. Coffee Machine, All Rights Reserved.")

    # cash in machine
    MACHINE_CASH = 100.00

    menu_choice = input("Coffee (C) or Report (R) or Power (O)ff?").lower()
    if menu_choice == 'c':
        
        # ask what user wants - espresso, latte, or cappuccino
        coffee_choice = input("What kind of coffee would you like: Espresso (A), Latte (B), or Cappuccino (C): ").lower()
        if coffee_choice == 'a':
            espresso()

        elif coffee_choice == 'b':
            latte()
    
        elif coffee_choice == 'c':
            cappuccino()

    # print report - water, milk, coffee, money
    elif menu_choice == 'r':
        print("printing report: \n")
        report()
        main()

    # turn off coffee machine "off"
    elif menu_choice == 'o':
        print("Powering Off...")
        sys.exit()

    else:
        print("Choice invalid.")
        main()

    more_coffee = input("Would you like more coffee (y)es or (n)o: ").lower()
    if more_coffee == "y" or "yes":
        main()

    elif more_coffee == "n" or "no":
        view_report = input("View (R)eport or (E)xit: ").lower()
        if view_report == "r" or "report":
            print("printing report \n")
            report()
            main()

        else:
            print("Exiting now...")


if __name__ == '__main__':
    main()