import random

secret_number= random.randint(1,10)
attempt=3
print("I am thinking of a number between 1 and 10")

while attempt > 0:
    guess=int(input("Guess the number:"))
    if guess == secret_number:
        print("Congratulations! You guessed the number")
    elif guess< secret_number:
        print("Too low,Try again")
    else:
        print("Too large, Try again")