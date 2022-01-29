
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

number = len(names) - 1

name = random.randint(0, number)

payer = names[name]

print(f"{payer} is going to buy the meal today!")