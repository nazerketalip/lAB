import random

rand = random.randint(1, 20)

print("Hello! What is your name?")

name = input()

print(f"Well, {name}, I am thinking of a number between 1 and 20.")
sum = 0
while True:
    n = int(input("Take guess.\n"))
    sum += 1
    if n == rand:
        print(f"Good job, {name}! You guessed my number in {sum} guesses!")
        break
    elif n > rand:
        print("Your guess is too high")
    else:
        print("Your guess is too low.")