import random
import string
x = int(input("How long should your random password be?\n"))

#My approach
list1 = []
if (x%3 == 0):
    for i in range(0, x//3):
        a = random.randint(0,9)
        list1.append(str(a))
    for j in range(0, x//3):
        b = random.choice(string.ascii_letters)
        list1.append(b)
    for k in range(0, x//3):
        c = random.choice(string.punctuation)
        list1.append(c)
elif (x%3 == 1):
    for i in range(0, x//3):
        a = random.randint(0,9)
        list1.append(str(a))
    for j in range(0, x//3 + 1):
        b = random.choice(string.ascii_letters)
        list1.append(b)
    for k in range(0, x//3):
        c = random.choice(string.punctuation)
        list1.append(c)
elif (x%3 == 2):
    for i in range(0, x//3+1):
        a = random.randint(0,9)
        list1.append(str(a))
    for j in range(0, x//3 + 1):
        b = random.choice(string.ascii_letters)
        list1.append(b)
    for k in range(0, x//3):
        c = random.choice(string.punctuation)
        list1.append(c)   
else:
    print("Not a valid number. Please choose again!")
for l in range(1, len(list1)):
    random.shuffle(list1)
print("Here is your random password:\t", end="")
for l in range(len(list1)):
    print(list1[l], end="")

#And the better method
random_password = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for n in range(x)])
print("\nHere is your random password:\t", end="")
print(random_password)
