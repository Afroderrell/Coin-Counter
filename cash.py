from cs50 import get_float

money = get_float("How much money is owed?")

while (money < 0):
    print("Value must be a dollar amount greater than 0")
    money = get_float("How much money is owed?")
    if money > 0:
        break

cents = round(money *100)
coin = 0
quarters = 25
dimes = 10
nickels = 5
pennies = 1

while cents > 0:
    if cents >= quarters:
        coin += 1
        cents = cents - quarters
    elif cents >= dimes:
        coin +=1
        cents = cents - dimes
    elif cents >= nickels:
        coin +=1
        cents = cents - nickels
    elif cents >= pennies:
        coin +=1
        cents = cents - pennies
else:
        print("Number of coins:", coin)
