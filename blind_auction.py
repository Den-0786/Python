from blindAuctionArt import logo
print(logo)
from dennisClear import clear

game_end = False
bids = {}

def find_highest_bidder(bids):
    highest_bid = 0
    winner = ""
    for bidder in bids:
        bid = bids[bidder]
    if bid > highest_bid:
        highest_bid = bid
        winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
    
while not game_end:
    print("Welcome to the blind auction program.\n")
    name = input("What is your name? \n")
    bid_amount = int(input("What is your bid? $"))
    bids[name] = bid_amount
    play_again = input("Are there any other bidders? (yes or no) ").lower()
    if play_again == "no":
        game_end = True
        find_highest_bidder(bids)
    elif play_again == "yes":
        clear()
    else:
        print("Invalid input.")