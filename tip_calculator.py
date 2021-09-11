print("Welcome to the tip calculator!\n")
while True:
    try:
        total_bill = float(input("What was the total bill? $"))
    except ValueError:
        print("Not a valid input - Only numbers allowed")
        continue
    break
while True:
    try:
        tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))
    except ValueError:
        print("Not a valid input - Only numbers allowed")
        continue
    break
while True:
    if (tip_percentage == 10):
        break
    elif (tip_percentage == 12):
        break
    elif (tip_percentage == 15):
        break
    else:
        print("Sorry, you can only use one of the mentioned values")
        tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))
while True:
    try:
        persons = int(input("How many people to split the bill? "))
    except ValueError:
        print("Not a valid input - Only numbers allowed")
        continue
    break
print("\nSo you have to pay $" + str(total_bill) + " plus " + str(tip_percentage) + "% tip and split the bill between " + str(persons) + " people!")
bill = round((((total_bill*tip_percentage)/100)+total_bill)/persons, 2)
print("Each person should pay: $"+str(bill)+"\n")
