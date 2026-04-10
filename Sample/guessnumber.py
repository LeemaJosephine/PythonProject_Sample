#Guess the Number
import random  # Use the random lib for creating a random number
randomNo = random.randint(1,99)  #store the random number b/w 1 - 99 in variable randomNo
guess = 0
att = 0

while randomNo != guess: #RandomNo not equal to guess loop will execute
    guess = int(input("Enter the number b/w 1 - 99 :"))  #Get the guess no from user and its store in variable guess
    att += 1

    if guess < randomNo: #If the guess number lesser than random number print statement will execute
        print("Guessed no is lesser than random Number")
        guess = int(input("Enter the number b/w 1 - 99 :"))  #again get the guess no from user and its store in variable guess

    elif guess > randomNo: # If the guess number greater than random number print statement will execute
        print("Guessed no is lesser than random Number")
        guess = int(input("Enter the number b/w 1 - 99 :"))  # again get the guess no from user and its store in variable guess

    print(f"Correct! You guessed the number in {att} attempts.") # If the guess Number is equal to Random Number print statement will execute



###################################################################################################################

#Word Scramble
import random

words = ['python', 'javascript', 'java', 'automation', 'pytest', 'guvi', 'selenium']

word = random.choice(words) #random choice the word from the list words
correct_word = word # Store the correct word

jumbled_list = list(word) #Convert the string into individual character
random.shuffle(jumbled_list) #Shuffle the individual character randomly
jumbled_word = "".join(jumbled_list) #Convert all the individual character into single string

print(f"Unscrambled word: {jumbled_word}") #shown the Unscrambled word from the list randomly

while True:
    guess = input("Enter the correct word: ").lower() # Get the word from the user

    if guess == correct_word: # If the Unscrambled word equal to the user entered value
        print("Correct! You unscrambled the word!") # Print statement execute
        break # Exit the loop if condition is correct
    else:
        print("Incorrect, try again!") # If the Unscrambled word not equal to the user entered value