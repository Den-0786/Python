from game_data import data
import random
import art
import loading_logo
from dennisClear import clear
import time

def display_format_data(account):
    """Format account data into printable format."""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"

    #checking  the followers against the user's guess
def check_followers(guess, followers_of_a, followers_of_b):
    """Check followers against user's guess
    and return True if they got it right.
    Or False if they got it wrong."""
    if followers_of_a > followers_of_b:
        return guess == "a"
    elif followers_of_b > followers_of_a:
        return guess == "b"
    else:
        if guess == "a" or guess == "b":
            return 'Draw'
#Displaying logo
def display_logo():
    print(art.welcome_logo)
    print(art.logo)
    time.sleep(2)
    clear()

    for i in range(1):
        print(loading_logo.logo[0])
        time.sleep(0.8)
        clear()
        
        print(loading_logo.logo[1])
        time.sleep(0.8)
        clear()
        
        print(loading_logo.logo[2])
        time.sleep(0.8)
        clear()
        
        print(loading_logo.logo[3])
        time.sleep(0.8)
        clear()
        
        print(loading_logo.logo[4])
        time.sleep(0.8)
        clear()
        
        print(loading_logo.logo[5])
        time.sleep(0.8)
        clear()
        
        print(loading_logo.logo[6])
        time.sleep(0.8)
        clear()
        
        print(loading_logo.logo[7])
        time.sleep(0.8)
        clear()
        
        print(loading_logo.enter_logo)
        time.sleep(1)
        input("Press Enter to continue")
        clear()
        
    #creating a function called play game
def play_game():
    clear()
    print(art.logo2)
    print("THIS IS A GAME BASED ON THE NUMBER OF FOLLOWERS ON INSTAGRAM")
    score = 0
    account_b = random.choice(data)
    game_should_continue = True
    while game_should_continue:
        #making account at position B become the next account at position A
        account_a = account_b
        account_b = random.choice(data)
        
        #making another random choice if there is same data in account A and B
        while account_a == account_b:
            account_b =- random.choice(data)
    
        #Print the comparing data to the screen       
        print(f"Compare A: {display_format_data(account_a)}.")
        print(art.vs)
        print(f"Against B: {display_format_data(account_b)}.")

        #Asking user to guess who has more followers
        follow_checker = input("Who has more followers? Type 'A' or 'B':\n ").lower()
        
        a_followers_count = account_a["follower_count"]
        b_followers_count = account_b["follower_count"]
        
        #Checking if user is correct
        is_correct = check_followers(guess= follow_checker, followers_of_a= a_followers_count, followers_of_b=b_followers_count)
        
        clear()
        print(art.logo2)
        
        if is_correct == 'Draw':
            score += 0.5
            print(f"It's a draw because both have the same number of followers. Current score: {score}")
        elif is_correct:
            score += 2
            print(f"You're right. Current score: {score}")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")

def main():
    display_logo()
    play_game()
while input("Do you want to play again? Type 'y' or 'n':\n").lower() == "y":
        clear()
        play_game()
        print("Thank you for playing our game")
        print("Hope you enjoyed our game?")
        print("See you next time")
        print("Bye")

