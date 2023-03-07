import string
for letter in string.ascii_uppercase:
    name = letter + ".txt"
    with open(name, "w") as file:
        print( name)