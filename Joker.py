# 1) Prints five random numbers between 1 to 45, making sure they are unique by testing and
# retesting for their single occurrence in the list and one random number (the joker)
# between 1 to 20.
# 2) Modified with the same code to choose between 1 to 20.
# 3) Redifined its complexity to find numbers and bring me the remaining
# 4) I started creating conditions with different player systems, for more numerical results.The code was getting too big,
# so I tried to make it more elegant by using functions. On the first try the code was still big,
# so I changed the mode according to the players' systems.

import random

# def Joker_Lottery(n, m):
    # *** code starts here ***
# 
    # list_1 = []
    # list_2 = []
# 
    # for i in range (0, n):
        # list_1.append(random.randint(1, 45))
        # i += 1
# 
    # j = 0
    # while j < n:
        # if list_1.count(list_1[j]) != 1:
            # list_1[j] = random.randint(1, 45)
            # j = 0
        # else:
            # j += 1
# 
    # *** list_1 ends HERE ***
# 
    # for k in range (0, m):
        # list_2.append(random.randint(1, 20))
        # k += 1
# 
    # l = 0
    # while l < m:
        # if list_2.count(list_2[l]) != 1:
            # list_2[l] = random.randint(1, 20)
            # l = 0
        # else:
            # l += 1
# 
    # *** the result ***
# 
    # your_numbers = []
    # for list_a in range(1, 46):
        # if list_1.count(list_a) == 0:
            # your_numbers.append(list_a)
        # else:
            # continue
    # joker = []
    # for list_b in range(1, 21):
        # if list_2.count(list_b) == 0:
            # joker.append(list_b)
        # else:
            # continue
# 
    # print(f"Your {45-n} numbers are {your_numbers} and Joker {joker}\n")

# END OF FUCTION

def Joker_Lottery(num, total):
    number_list = []
    for i in range (0, num):
        number_list.append(random.randint(1, total))
        i += 1
    j = 0
    while j < num:
        if number_list.count(number_list[j]) != 1:
            number_list[j] = random.randint(1, total)
            j = 0
        else:
            j += 1
    your_result = []
    for a in range (1, total+1):
        if number_list.count(a) == 0:
            your_result.append(a)
    print(f"** Good Luck **  {your_result}")

# system = int(input("Type 0 for no system, else the system number: "))
# if system == 0:
    # n = 40
    # m = 19
    # Joker_Lottery(n, m)
    # Joker_Lottery(40, 45)
    # Joker_Lottery(19, 20)
# elif system == 45:
    # n = 38
    # m = 19
    # Joker_Lottery(n, m)
    # Joker_Lottery(38, 45)
    # Joker_Lottery(19, 20)
# else:
    # print("This system not yet available!")

joker_systems = str("""
No System:   5-Numbers,   1-Columns | Cost:  0.50€, Chance:   ??% 
System 12:  15-Numbers, 118-Columns | Cost: 59.00€, Chance: 3.93%
System 13:  13-Numbers,  54-Columns | Cost: 27.00€, Chance:  4.2%
System 14:  12-Numbers,  38-Columns | Cost: 19.00€, Chance:  4.8%
System 15:  11-Numbers,  22-Columns | Cost: 11.00€, Chance: 4.76%
System 23:  10-Numbers,  51-Columns | Cost: 25.50€, Chance: 20.24%
System 24:  10-Numbers,  14-Columns | Cost:  7.00€, Chance: 5.55%
System 25:   9-Numbers,  30-Columns | Cost: 15.00€, Chance: 23.8%
System 34:   9-Numbers,   9-Columns | Cost:  4.50€, Chance:  7.1%
System 35:   8-Numbers,   6-Columns | Cost:  3.00€, Chance: 10.7%
System 45:   7-Numbers,   5-Columns | Cost:  2.50€, Chance: 23.8%""")

while True:
    try:
        system = str(input(joker_systems + "\n\nType 00 for No System, else the System #: "))
        print("\n")
        while True:
            if (system == f'{00:02d}' or system == f'{12:02d}' or system == f'{13:02d}' or system == f'{14:02d}' or system == f'{15:02d}' or system == f'{23:02d}' or system == f'{24:02d}' or system == f'{25:02d}' or system == f'{34:02d}' or system == f'{35:02d}' or system == f'{45:02d}'):
                break
            else:
                print("-> Not a valid input <-")
                system = str(input(joker_systems + "\n\nType 00 for No System, else the System #: "))
                print("\n")
                continue
    except ValueError:
        print("-> Not a valid input <-")
        continue
    break
if system == f'{00:02d}':
    # n = 40
    # m = 19
    # Joker_Lottery(n, m)
    Joker_Lottery(40, 45)
    Joker_Lottery(19, 20)
    print("\n")
elif system == f'{12:02d}':
    Joker_Lottery(30, 45)
    Joker_Lottery(19, 20)
    print("\n")
elif system == f'{13:02d}':
    Joker_Lottery(32, 45)
    Joker_Lottery(19, 20)
    print("\n")
elif system == f'{14:02d}':
    Joker_Lottery(33, 45)
    Joker_Lottery(19, 20)
    print("\n")
elif system == f'{15:02d}':
    Joker_Lottery(34, 45)
    Joker_Lottery(19, 20)
    print("\n")
elif system == f'{23:02d}':
    Joker_Lottery(35, 45)
    Joker_Lottery(19, 20)
    print("\n")
elif system == f'{24:02d}':
    Joker_Lottery(35, 45)
    Joker_Lottery(19, 20)
    print("\n")
elif system == f'{25:02d}':
    Joker_Lottery(36, 45)
    Joker_Lottery(19, 20)
    print("\n")
elif system == f'{34:02d}':
    Joker_Lottery(36, 45)
    Joker_Lottery(19, 20)
    print("\n")
elif system == f'{35:02d}':
    Joker_Lottery(37, 45)
    Joker_Lottery(19, 20)
    print("\n")
elif system == f'{45:02d}':
    Joker_Lottery(38, 45)
    Joker_Lottery(19, 20)
    print("\n")
else:
    print("Sorry, this system is not yet available!\n")
