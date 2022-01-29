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

pick = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
choice = int(pick)

if choice == 0:
  print(rock)
elif choice == 1:
  print(paper)
elif choice == 2:
  print(scissors)
else:
  print("That's not a choice!")

comp_choice = random.randint(0, 2)
print(comp_choice)

if comp_choice == 0:
  print(rock)
if comp_choice == 1:
  print(paper)
if comp_choice == 2:
  print(scissors)

if choice == 0 and comp_choice == 1:
  print("Uh oh, you lost!")
if choice == 1 and comp_choice == 2:
  print("Uh oh, you lost!")
if choice == 2 and comp_choice == 0:
  print("Uh oh, you lost!")
if choice == comp_choice:
  print("It is a draw!")
if comp_choice == 0 and choice == 1:
  print("Woohoo! You won!")
if comp_choice == 1 and choice == 2:
  print("Woohoo! You won!")
if comp_choice == 2 and choice == 0:
  print("Woohoo! You won!")