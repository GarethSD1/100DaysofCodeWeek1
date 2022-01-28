print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

direction = input("You are at a crossroads. Which way do you go? left or right?\n").lower()

if direction == "left":
  choice2 = input("You come to a lake. Do you swim or try to find a boat? Type 'swim' or 'boat'\n").lower()
  if choice2 == "boat":
    choice3 = input("You find an island with a house which has 3 doors. Which door do you pick: red, green or yellow?\n").lower()
    if choice3 == "red":
      print("Oh no! You are on fire!")
    elif choice3 == "green":
      print("Nuclear waste! Oh no!")
    elif choice3 == "yellow":
      print("Wow, you found the treasure!")
    else:
      print("Hmm, I didn't find that door!")
  else: 
    print("Sharks in the water! They got you!")
else:
  print("Oops! Wrong way!")