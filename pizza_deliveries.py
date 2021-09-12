print("Welcome to Python Pizza Deliveries!\n")
number_of_pizzas = int(input("How many Pizzas would you like? "))
i = 1
if number_of_pizzas == i:
    size = input("What size pizza do you wamt? S, M, or L ")
    add_pepperoni = input("Do you want pepperoni? Y or N ")
    extra_cheeze = input("Do you want extra cheese? Y or N ")

    # if add_pepperoni == "Y" or add_pepperoni == "y":
        # if size == "S" or size == "s":
            # bill = 15 + 2
        # elif size == "M" or size == "m":
            # bill = 20 + 3
        # else:
            # bill = 25 + 3
    # else:
        # if size == "S" or size == "s":
            # bill = 15
        # elif size == "M" or size == "m":
            # bill = 20
        # else:
            # bill = 25
    # if extra_cheeze == "Y" or extra_cheeze == "y":
        # bill += 1
    # print(f"Your final bill is ${bill}.")
    # ***NOTE*** Better approach:
    bill = 0
    if size == "S" or size == "s":
        bill += 15
    elif size == "M" or size == "m":
        bill += 20
    else:
        bill += 25
    if add_pepperoni == "Y" or add_pepperoni == "y":
        if size == "S" or size == "s":
            bill += 2
        else:
            bill += 3
    if extra_cheeze == "Y" or extra_cheeze == "y":
        bill += 1
    print(f"Your final bill is ${bill}.")
else:
    size = []
    add_pepperoni = []
    extra_cheeze = []
    bill = []
    total_bill = 0
    while i <= number_of_pizzas:
        size.append(input(f"What size #{i} pizza do you want? S, M, or L "))
        add_pepperoni.append(input("Do you want pepperoni? Y or N "))
        extra_cheeze.append(input("Do you want extra cheese? Y or N "))

        if add_pepperoni[i-1] == "Y" or add_pepperoni[i-1] == "y":
            if size[i-1] == "S" or size[i-1] == "s":
                bill.append(15 + 2)
            elif size[i-1] == "M" or size[i-1] == "m":
                bill.append(20 + 3)
            else:
                bill.append(25 + 3)
        else:
            if size[i-1] == "S" or size[i-1] == "s":
                bill.append(15)
            elif size[i-1] == "M" or size[i-1] == "m":
                bill.append(20)
            else:
                bill.append(25)
        if extra_cheeze[i-1] == "Y" or extra_cheeze[i-1] == "y":
            bill[i-1] += 1
        print(f"Your #{i} pizza costs ${bill[i-1]}.\n")
        total_bill += bill[i-1]
        i += 1
    print(f"Your total bill for the {i-1} pizzas is ${total_bill}.")
