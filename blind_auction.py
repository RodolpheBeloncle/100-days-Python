from replit import clear
from art import *
#HINT: You can call clear() to clear the output in the console.
print(logo)

start_Auction = True

# data auction dictionary
data_auction = {}

while start_Auction:

  # name of the bidder
  call_name = input("Your Name ? : ")
  
  # bidding price
  bid_price = int(input("what's your price ?  "))
  
  # adding name othe bidder with bidding price
  data_auction[call_name] = bid_price

  # ask if there are more bidders
  if_1_more_bid = input("Are there any offer users who want to bid ? ")
  
  # conditions yes / no
  if if_1_more_bid == "yes":

    clear

  # get the highest value at the end of the auction
  elif if_1_more_bid == "no":
    highest_value = 0

    for key,value in data_auction.items():
      print(key,value)
      
      if value > highest_value:
        highest_value = value
        name = key
        

    # the winner is ...
    print(f"{name} has bidded {highest_value} win the auction !")
    
    # end of the auction
    print("End of the auction !!")
    start_Auction = False

    
    # ------------------ Angela 's solution ------------------
    
    from replit import clear
from art import logo

print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  
  highest_bid = 0
  winner = ""
  
  # bidding_record = {"Angela": 123, "James": 321}
  
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
      
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  
  bids[name] = price
  
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
    
  elif should_continue == "yes":
    clear()
