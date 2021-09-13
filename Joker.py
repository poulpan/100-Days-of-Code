# Prints five random numbers between 1 to 45, making sure they are unique by testing and
# retesting for their single occurrence in the list and one random number (the joker)
# between 1 to 20.

import random

list = []
for i in range (0,5):
    list.append(random.randint(1,45))
    # ***NOTE*** 1st try
    # print(list)
    # duplicate =  list.count(list[i])
    # print(duplicate)
    # if duplicate != 1:
        # list[i] = random.randint(1,45)
    # else:
        # i += 1
    i += 1
print(list,"first")

# ***NOTE*** 2nd try
# while True:
    # print(list,"HERE")
    # j = 0
    # duplex = list.count(list[j])
    # if duplex != 1:
        # print(j,"CHECK")
        # list[j] = random.randint(1,45)
        # print(list,"NOT OK")
    # else:
        # j += 1
    # break
j = 0
while j < 5:
    if list.count(list[j]) != 1:
        print("***NOT OK***")
        list[j] = random.randint(1,45)
        j = 0
        print(list)
    else:
        print(j,"move ON")
        j += 1

# The above print() are for seeing the code progress and testing and can be removed.
# Only the below print() are needed for the result.

print("sorted", sorted(list))
print(f" joker [{random.randint(1,20)}]\n")
