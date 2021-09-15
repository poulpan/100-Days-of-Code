# ***NOTE*** ctrl + / adds a # at the start of the line
# ***NOTE*** 8 // 3: this // is called "floor division" 

#print("Day 1 - Python Print Function")
#print("The function is declared like this:")
#print("print('what to print')")
#print('print("what to print")')
#print("one\ntwo\nthree")
#print("one\ttwo\tthree")
#print("one" + " two" + " " + "three")


#Fix the code below 👇

#print("Day 1 - String Manipulation")
#print("String Concatenation is done with the '+' sign.")
#print('e.g. print("Hello " + "world")')
#print("New lines can be created with a backslash and n.")


# name = input("WHat is your fullname?\t")
# if (len(name.replace(" ", "")) > 12):
    # print("\nYou 've got a really long fullname!")
# else:
    # print("\nYour fullname has normal length.")
 
# a = input("a: ")
# b = input("b: ")
# c = a
# a = b
# b = c
# print("a = " + a)
# print("b = " + b)

# print("Hello there. Let's find a cool name for your band!!\n\n")
# city = input("What is the name of the city you live?\n")
# pet_name = input("what is the name of your pet?\n")
# print("Your band's name could be: " + pet_name + " " + city)

# a = input("#: ")
# print(type(a))
# print(int(str(a)[0])+int(str(a)[1]))
# 
# print(6/4)
# print(int(6/4))


# weight = float(input("What is your weight? "))
# height = float(input("What is your height? "))
# BMI = round(weight/height**2, 1)
# print("Your BMI equals ", BMI, "\n")
# if BMI < 18.5:
    # print(f"According to your BMI={BMI} you are underweight.")
# elif BMI < 25:
    # print(f"According to your BMI={BMI} you have a normal weight.")
# elif BMI < 30:
    # print(f"According to your BMI={BMI} you are overweight.")
# elif BMI < 35:
    # print(f"According to your BMI={BMI} you are obese.")
# else:
    # print(f"According to your BMI={BMI} you are clinically obese.")

# for i in range (0,10):
    # a = 19+i/10
    # print(a," ",type(a))
    # print(round(a)," ",type(round(a)))
   
# print(a:=round(10/3,2)," ",type(a))
# print(b:=10//3," ",type(b))

# n = int(input("Give me a whole number plz: "))
# list1 = []
# list2 = []
# for i in range(1, n+1):
    # if i%2 == 0:
        # list1.append(i)
    # else:
        # list2.append(i)
# print("The even numbers are:\n", list1, "\n")
# print("The odd number are:\n", list2, "\n")

# year = int(input("Which year do you want to check? "))
# f = open("output.txt", "w")
# for year in range (1000,3001):
    # print("year= ",year, file=f)
    # if year % 400 == 0:
        # print("Leap year.", file=f)
    # elif year % 4 == 0:
        # if year % 100 != 0:
            # print("Leap year.", file=f)
        # else:
            # print("NOT leap year.", file=f)
    # else:
            # print("NOT leap year.", file=f)
# ***NOTE*** Other way:
    # if year % 4 != 0:
        # print("NOT leap year.", file=f)
    # elif year % 100 != 0:
        # print("Leap year.", file=f)
    # elif year % 400 != 0:
        # print("NOT leap year.", file=f)
    # else:
        # print("Leap year.", file=f)
# f.close()


# import random 
# random_int = random.randint(0,4)
# random_flo = random.random()
# print(random_int,"\n")
# print(random_flo,"\n")
# print("{:.2f}".format(random_int+random_flo))

# import random
# coin = random.randint(1,2)
# if coin == 1:
    # print("Heads")
# else:
    # print("Tails")

# list = ["a","b","c","d","e","f","g"]
# print(list)
# print(list.pop(1))
# print(list)
# print(list.index("d"))
# list.reverse()
# print(list)
# list.extend(["h","i"])
# print(list)

# import random
# names_string = input("Give me your names seperated by a comma: ")
# names = names_string.split(",")
# lucky_name = random.randint(0,len(names)-1)
# print(f"And the winned of ppaying the bill is {names[lucky_name]}")
# ***NOTE***or ever better:
# print(f"And the winned of ppaying the bill is {random.choice(names)}")

