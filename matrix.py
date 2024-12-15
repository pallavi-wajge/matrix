line1 = ["⬜️","️⬜️","️⬜️"] 

line2 = ["⬜️","⬜️","️⬜️"] 

line3 = ["⬜️️","⬜️️","⬜️️"] 

map = [line1, line2, line3] 

print("Hiding your treasure! X marks the spot.") 

position = input("Chose position of treasure") # Where do you want to put the treasure? Chose any one from A1, A2, A3, B1, B1, B3, C1, C2, C3  

place1 = position[0].lower() 

#print(place1) 

if place1 == "a": 

  y=0 

if place1 == "b": 

  y=1 

if place1 == "c": 

  y=2 

#Or we can use  

# abc = ["a", "b", "c"] 

# y = abc.index(place1) 

#print(y) 

place2 = int(position[1]) 

x = place2 - 1 

#Or we can use 

#x = int(position[1]) - 1 

#print(x) 

map[x][y] = "X" 

print(f"{line1}\n{line2}\n{line3}") 
