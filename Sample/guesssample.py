import random

randomNo = random.randint(1, 99)
guess = 0
att = 0

while guess != randomNo:
    guess = int(input("Enter the number b/w 1 - 99: "))
    att += 1

    if guess < randomNo:
        print("Guessed number is LESS than the random number")
    elif guess > randomNo:
        print("Guessed number is GREATER than the random number")
    else:
        print(f"Correct! You guessed the number in {att} attempts.")