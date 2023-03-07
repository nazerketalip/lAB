l = input().split()
with open("testing.txt", "w") as file:
    for i in l:
        file.write(i + "\n")