line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?

input_lst=['a','b','c']
letter=position[0].lower()
x=input_lst.index(letter)
integer= int(position[1])-1
map[integer][x] ="X"

print(f"{line1}\n{line2}\n{line3}")