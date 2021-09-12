import random

number = random.randint(1,100)
guesses = 0

print("Welcome to the number guessing game!\n")
print("I'm thinking of a number from 1 to 100. What is it?")

while True:
    n = int(input())
    guesses += 1
    if n > number:
        print("Your number is too large.")
    elif n < number:
        print("Your number is too small.")
    else:
        print(f"\nYou got it! The number was {number}\nIt took you {guesses} guesses to get the number!\n")
        break
