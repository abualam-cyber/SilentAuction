from ScreenClear import screen_clear

from Art import logo

print (logo)

bid_dict = {}
more_bidders = False

def find_highest_bidder(bid_values):
    highest_bid = 0.00
    winner = ""
    for bidder in bid_values:
        bid_amount = bid_values[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}!")
        

while not more_bidders:
    name = input("Enter name of bidder \n")
    bid = float(input("Enter your bid \n"))
    bid_dict[name] = bid
    more_users = input("Are there more bidders? Type 'y' for yes, 'n' for no.\n")
    if(more_users == 'y'):
        screen_clear()
    elif(more_users == 'n'):
        more_bidders = True
        find_highest_bidder(bid_dict)
        
