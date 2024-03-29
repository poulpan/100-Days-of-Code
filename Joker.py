# 1) Prints five random numbers between 1 to 45, making sure they are unique by testing and
# retesting for their single occurrence in the list and one random number (the joker)
# between 1 to 20.
# 2) Modified with the same code to choose between 1 to 20.
# 3) Redifined its complexity to find numbers and bring me the remaining (My current logic is that if i.e. you need to find 5 
# numbers out of 45, the code creates a list of 40 numbers and then outputs the remaining 5 that are missing from that list! - 
# Same logic for the 1 joker number, the code creates a list of 19 numbers and then outputs the remaining 1 that's missing from
# the list!)
# 4) I started creating conditions with different player systems, for more numerical results.The code was getting too big,
# so I tried to make it more elegant by using functions. On the first try the code was still big, so I changed the mode 
# according to the players' systems.
# 5) Added another loop asking the user hot many times to run the same code. So i.e. now the code will run X times repeating
# the step (3) and out of the X results of 5 numbers, finds out the 5 most repeative numbers to bring you as a result. Same for
# the 1 joker number.

# *** START OF OLD CODE ***
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
# *** END OF OLD CODE ***

import random
from datetime import datetime
from collections import Counter

f1= open("joker_file_1.txt", "a")
# f2= open("joker_file_2.txt", "w")
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print(f"*** DATE:\t{dt_string} ***\n", file=f1)
# print(f"*** DATE:\t{dt_string} ***\n", file=f2)

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
        number_to_run = int(input("How many times to run the code before getting a result? "))
        print(f"Repetition of the code {number_to_run}-times", file=f1)
        while True:
            if (number_to_run > 0):
                break
            else:
                print("-> Not a valid input <-")
                number_to_run = int(input("How many times the code to run before getting a result? "))
                continue
    except ValueError:
        print("-> Not a valid input <-")
        continue
    break

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

def Joker_Lottery(num, total):
    t = 0
    temp_list = []
    while t < number_to_run:
        number_list = []
        for i in range (0, num):
            number_list.append(random.randint(1, total))
            i += 1

        # if number_to_run <= 5000:
            # print(f"FIRST_LIST: {number_list}", file=f2)

        j = 0
        while j < num:

            # if number_to_run <= 5000:
                # print(f"{j}-try: {number_list}", file=f2)

            if number_list.count(number_list[j]) != 1:
                number_list[j] = random.randint(1, total)
                j = 0
            else:
                j += 1
        your_result = []
        for a in range (1, total+1):
            if number_list.count(a) == 0:
                your_result.append(a)
        # print(f"** Good Luck **  {your_result}\n", file=f2)
        temp_list.append(your_result)
        t += 1

    print(f"temp_list= {temp_list}", file=f1)

    end_list = []
    final_list = []
    for x in range (0, len(temp_list)):
        for y in range (0, total-num):
            end_list.append(temp_list[x][y])

    print(f"end_list= {end_list}", file=f1)
    print(f"total results in end_list: {len(end_list)}", file=f1)
    print(Counter(end_list), file=f1)

    most_common_list = Counter(end_list).most_common(total-num)
    for z in range (0, len(most_common_list)):
        final_list.append(most_common_list[z][0])

    print(f"final_list= {sorted(final_list)}", file=f1)
    print(f"total results in final_list: {len(final_list)}\n", file=f1)

    print(f"** Good Luck **  {sorted(final_list)}")

if system == f'{00:02d}':
    print(f'S-{system}\n', file=f1)
    # print(f'S-{system}', file=f2)
    print(f'S-{system}')
    Joker_Lottery(40, 45)
    Joker_Lottery(19, 20)
    print("\n")
elif system == f'{12:02d}':
    print(f'S-{system}\n', file=f1)
    # print(f'S-{system}', file=f2)
    print(f'S-{system}')
    Joker_Lottery(30, 45)
    Joker_Lottery(19, 20)
    print("\n")
elif system == f'{13:02d}':
    print(f'S-{system}\n', file=f1)
    # print(f'S-{system}', file=f2)
    print(f'S-{system}')
    Joker_Lottery(32, 45)
    Joker_Lottery(19, 20)
    print("\n")
elif system == f'{14:02d}':
    print(f'S-{system}\n', file=f1)
    # print(f'S-{system}', file=f2)
    print(f'S-{system}')
    Joker_Lottery(33, 45)
    Joker_Lottery(19, 20)
    print("\n")
elif system == f'{15:02d}':
    print(f'S-{system}\n', file=f1)
    # print(f'S-{system}', file=f2)
    print(f'S-{system}')
    Joker_Lottery(34, 45)
    Joker_Lottery(19, 20)
    print("\n")
elif system == f'{23:02d}':
    print(f'S-{system}\n', file=f1)
    # print(f'S-{system}', file=f2)
    print(f'S-{system}')
    Joker_Lottery(35, 45)
    Joker_Lottery(19, 20)
    print("\n")
elif system == f'{24:02d}':
    print(f'S-{system}\n', file=f1)
    # print(f'S-{system}', file=f2)
    print(f'S-{system}')
    Joker_Lottery(35, 45)
    Joker_Lottery(19, 20)
    print("\n")
elif system == f'{25:02d}':
    print(f'S-{system}\n', file=f1)
    # print(f'S-{system}', file=f2)
    print(f'S-{system}')
    Joker_Lottery(36, 45)
    Joker_Lottery(19, 20)
    print("\n")
elif system == f'{34:02d}':
    print(f'S-{system}\n', file=f1)
    # print(f'S-{system}', file=f2)
    print(f'S-{system}')
    Joker_Lottery(36, 45)
    Joker_Lottery(19, 20)
    print("\n")
elif system == f'{35:02d}':
    print(f'S-{system}\n', file=f1)
    # print(f'S-{system}', file=f2)
    print(f'S-{system}')
    Joker_Lottery(37, 45)
    Joker_Lottery(19, 20)
    print("\n")
elif system == f'{45:02d}':
    print(f'S-{system}\n', file=f1)
    # print(f'S-{system}', file=f2)
    print(f'S-{system}')
    Joker_Lottery(38, 45)
    Joker_Lottery(19, 20)
    print("\n")
else:
    print("Sorry, this system is not yet available!\n")

f1.close()
# f2.close()
