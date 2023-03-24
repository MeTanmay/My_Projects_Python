import random
from art import logos
num=random.randint(0,100)


print(logos)
print("Welcome to the number guessing game!")
print("I am thinking a number between 0 to 100.")
level=input("Choose a difficulty level. Type 'easy' or 'hard': \n ")
#  guess=int(input("Make a guess: " ))

#   def check():
#     if guess==num:
#         print("Congrats you guessed the word correctly")
        
        
#     elif guess>num:
#         print("Too high")
#         print("Guess again")
#     else:
#         print("Too low.")
#         print("Guess again")

if level=="easy":
    guess_left=10
else:
    guess_left=5 


for i in range(0,guess_left):
    
    print(f"You have {guess_left} attempts left to guess the number.")
    guess_left-=1
    guess=int(input("Make a guess." ))
    if guess==num:
        print("Congrats you guessed the word correctly")
        break
        
    elif guess>num:
        print("Too high")
        if (guess_left==0):
            print(f"The Number was {num}")
            print("You have run out of guesses, You loser. Shame on you! Bozo!")
    else:
        print("Too low.")
        if (guess_left==0):
            print(f"The Number was {num}")
            print("You have run out of guesses, You loser. Shame on you! Bozo!") 
print("Game over")  