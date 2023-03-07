path = input()

with open(path, "r") as file:
    count = 0
    for line in file:
        count += 1
#/Users/nazerkeabubakirovna/PycharmProjects/Project/lab6/3.py
print("Number of lines in the file: ", count)