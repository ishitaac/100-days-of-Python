

print("Welcome to Secret Auction Program")
from art1 import logo
print(logo)

bids ={}
bidding_finished = False

def highest_bidder(new_bidder):
  highest = 0
  winner = ""
  for bidder in new_bidder:
    bid_amt = new_bidder[bidder]
    if bid_amt > highest:
      highest = bid_amt
      winner = bidder
  print(f"the winner is {winner} with a bid of highest ${highest}")

while bidding_finished == False:
  name = input("What is your name?: ")
  bid_price = int(input("What is your bidding amount?: $"))
  bids[name]= bid_price
  print(bids)
  other = input("Are there any bidder? Type 'yes' or 'no'. ").lower()
  if other == "no":
    bidding_finished = True
    highest_bidder(bids)
