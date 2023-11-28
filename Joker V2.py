import random
from datetime import datetime
from collections import Counter

f1= open("joker_file_1.txt", "a")
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print(f"*** DATE:\t{dt_string} ***\n", file=f1)

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
        number_list = random.sample(range(1, total + 1), num)
        your_result = []
        for a in range (1, total+1):
            if number_list.count(a) == 0:
                your_result.append(a)
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
    print(f'S-{system}')
    Joker_Lottery(40, 45)
    Joker_Lottery(19, 20)
    print("\n")
elif system == f'{12:02d}':
    print(f'S-{system}\n', file=f1)
    print(f'S-{system}')
    Joker_Lottery(30, 45)
    Joker_Lottery(19, 20)
    print("\n")
elif system == f'{13:02d}':
    print(f'S-{system}\n', file=f1)
    print(f'S-{system}')
    Joker_Lottery(32, 45)
    Joker_Lottery(19, 20)
    print("\n")
elif system == f'{14:02d}':
    print(f'S-{system}\n', file=f1)
    print(f'S-{system}')
    Joker_Lottery(33, 45)
    Joker_Lottery(19, 20)
    print("\n")
elif system == f'{15:02d}':
    print(f'S-{system}\n', file=f1)
    print(f'S-{system}')
    Joker_Lottery(34, 45)
    Joker_Lottery(19, 20)
    print("\n")
elif system == f'{23:02d}':
    print(f'S-{system}\n', file=f1)
    print(f'S-{system}')
    Joker_Lottery(35, 45)
    Joker_Lottery(19, 20)
    print("\n")
elif system == f'{24:02d}':
    print(f'S-{system}\n', file=f1)
    print(f'S-{system}')
    Joker_Lottery(35, 45)
    Joker_Lottery(19, 20)
    print("\n")
elif system == f'{25:02d}':
    print(f'S-{system}\n', file=f1)
    print(f'S-{system}')
    Joker_Lottery(36, 45)
    Joker_Lottery(19, 20)
    print("\n")
elif system == f'{34:02d}':
    print(f'S-{system}\n', file=f1)
    print(f'S-{system}')
    Joker_Lottery(36, 45)
    Joker_Lottery(19, 20)
    print("\n")
elif system == f'{35:02d}':
    print(f'S-{system}\n', file=f1)
    print(f'S-{system}')
    Joker_Lottery(37, 45)
    Joker_Lottery(19, 20)
    print("\n")
elif system == f'{45:02d}':
    print(f'S-{system}\n', file=f1)
    print(f'S-{system}')
    Joker_Lottery(38, 45)
    Joker_Lottery(19, 20)
    print("\n")
else:
    print("Sorry, this system is not yet available!\n")

f1.close()