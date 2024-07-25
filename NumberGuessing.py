
from numberlogo import logo
import random
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


#Function to check the user guessed answer against the actual answer
def check_answer(guess, answer, turns):
    """ checks answer against guess. Returns the answer of turns remaining"""
    if guess > answer:
        print ("Too high!\n")
        return turns - 1
    elif guess < answer:
        print ("Too low!\n")
        return turns - 1
    else:
        print (f"You got it! The answer was {answer}\n")


#function to set the level
def set_difficulty():
    level = input("Choose a level: 1 for  easy or 2 for hard\n")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
    
# Choosing a random number between 1 and 100
def game():
    print(logo)
    print("Welcome to the Number Guessing Game!\n")
    print("I'm thinking of a number between 1 and 100\n")
    answer = random.randint(1, 100)
    print(f"The answer is {answer}\n")
    
    turns = set_difficulty()
    
    guess = 0
    while guess != answer:
        print(f"You have {turns}  attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        # track the number of turns and reduce by 1
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print(f"You have run out of guess, you lose\n")
            return
        elif guess != answer:
            print("Guess Again!\n")        
game()