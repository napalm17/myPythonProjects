figures = ["Jules Winnfield", "Hans Landa", "The Bride", "Dr. King Schultz", "Lt. Aldo Raine", "Mr. Pink", "Mia Wallace", "Django Freeman", "Calvin Candie", "Hattori Hanzo"]
action = ["kill","fuck","mock","beat","marry","serve","ignore","praise","curse","shoot"]
figures.insert(1,"name")
print(figures)
#figures.remove("The Bride")
#figures.clear()
#figures.pop()
#print(figures.index("Hans Landa"))
#print(figures[1:6])
#print(figures.count("Hans Landa"))
#figures.sort()
#print(figures)
#print(figures.reverse())
#action = figures.copy()
f = int(input("Pick a random number to find out your Tarantino character soulmate: "))
a = int(input("Pick another number to determine what this character will do to you: "))
print("Ok, seems like " + figures[f] + " will " + action[a] + " you." )