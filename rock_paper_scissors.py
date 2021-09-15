from imaplib import Int2AP

import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# we can also make a list for the images: images = ["rock", "paper", "scissors"] and print() 
# as images[usr_choice-1] & images[pc_choice-1]

while True:
    usr_choice = int(input("What do you choose? Type 1 for Rock, 2 for Parer or 3 for Scissors: "))
    pc_choice = random.randint(1,3)

    if usr_choice < 1 or usr_choice > 3:
        print("You may chose between 1, 2 or 3. Please try again!\n")
    else:
        if usr_choice == pc_choice:
            if usr_choice == 1:
                print(rock,"\n""Computer chose:\n",rock,"\nIt's a Tie! Try again.")
            elif usr_choice == 2:
                print(paper,"\n""Computer chose:\n",paper,"\nIt's a Tie! Try again.")
            else: #choice 3
                print(scissors,"\n""Computer chose:\n",scissors,"\nIt's a Tie! Try again.")
        else:
            if usr_choice == 1:
                if pc_choice == 2:
                    print(rock,"\n""Computer chose:\n",paper,"\nYou lost\nGood Game!")
                    break
                else: #choice 3
                    print(rock,"\n""Computer chose:\n",scissors,"\nYou won\nGood Game!")
                    break
            elif usr_choice == 2:
                if pc_choice == 1:
                    print(paper,"\n""Computer chose:\n",rock,"\nYou won\nGood Game!")
                    break
                else: #choice 3
                    print(paper,"\n""Computer chose:\n",scissors,"\nYou lost\nGood Game!")
                    break
            else: #choice 3
                if pc_choice == 1:
                    print(scissors,"\n""Computer chose:\n",rock,"\nYou lost\nGood Game!")
                    break
                else: #choice 2
                    print(scissors,"\n""Computer chose:\n",paper,"\nYou won\nGood Game!")
                    break
