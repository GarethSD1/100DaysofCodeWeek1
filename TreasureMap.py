
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

place = [int(i) for i in (position)]
x = "X"
map [place[1] -1] [place[0]-1] = x

print(f"{row1}\n{row2}\n{row3}")