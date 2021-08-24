
import random
import functools

from art import logo

print(logo)
# ----- Data users -----
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

nb_distribution = 2

user = []
computer = []
player_Points = 0
computer_Points = 0
should_continue = True
yes = "y"
no = "n"

#------------------------------------
# ----- Function Part ---------------

def blackJack(userhand,dealerHand):
  if userhand.count(11)== 1 and userhand.count(10)== 1:
    print("BLACKJACK")
    print("you win")
    return False

  elif dealerHand.count(11)== 1 and dealerHand.count(10)== 1 and player_Points == 21:
    print("hand is pushed or player win")
  
  elif dealerHand.count(11)== 1 and dealerHand.count(10)== 1:
    print("player loose")

  
  
def pointsCheckerStart(playerPts,dealerPts):
  
  if playerPts > 21:
    if user.count(11) > 0 and (playerPts - 11)+1 <= 21  :
      playerPts = (playerPts - 11)+1
      print("player continue")
      return True 
    elif user.count(11) > 0 and (playerPts - 11)+1 > 21 :
      print("Player loose")
      return False
    
    
  elif dealerPts > 21:
    if computer.count(11) > 1 and (dealerPts - 11)+1 <= 21  :
      dealerPts = (dealerPts - 11)+1
      print("game continue")
      return True

    elif computer.count(11) > 0 and (dealerPts - 11)+1 > 21 :
      print("player wins")
      return False

def giveAnotherCard(name,user_turn,points):
  for i in range(0,1):
    user_turn.append(random.choice(cards))
  print(f"{name}'s hand: {user_turn}")
  points = functools.reduce(lambda a, b: a+b,user_turn)
  print(f"{name} points : {points} \n")
  return points
  
  
  
  
def computer_play(name,user_turn,points):
  while points < 17:
    user_turn.append(random.choice(cards))
    points = functools.reduce(lambda a, b: a+b,user_turn)
  print(f"{name}'s hand: {user_turn}")
  print(f"{name} points : {points} \n")
  return points
  
    
def final_Point_Checker(playerPts,dealerPts) :

  userWin = "You Win"
  dealerWin = "You Loose"
  player_score = 21 - playerPts
  dealer_score = 21 - dealerPts

  if playerPts <= 21 and dealerPts <= 21:
    if player_score < dealer_score:
      print(f"dealer's points : {dealerPts}")
      print(f"Player's points : {playerPts}")
      print(userWin) 

    elif player_score > dealer_score:
      print(f"dealer's points : {dealerPts}")
      print(f"Player's points : {playerPts}")
      print(dealerWin)

    elif player_score == dealer_score:
      print(f"dealer's points : {dealerPts}")
      print(f"Player's points : {playerPts}")
      print("It's draw")

  if player_score < 0:
    print(f"dealer's points : {dealerPts}")
    print(f"Player's points : {playerPts}")
    print("you loose")

  elif dealer_score < 0:
    print(f"dealer's points : {dealerPts}")
    print(f"Player's points : {playerPts}")
    print("you win")
    
# --------------------------------------------


  # user and dealer get 2 random cards (pick 2 random's cards for each user)
  
for i in range(0,nb_distribution):
  user.append(random.choice(cards))
  computer.append(random.choice(cards))
  
  # user and dealer Score points
  
player_Points = functools.reduce(lambda a, b: a+b, user)
print(f"\nPlayer's hand: {user}")
print(f"Player points : {player_Points} \n")

computer_Points = functools.reduce(lambda a, b: a+b, computer)
print(f"Dealer's hand: {computer}")
print(f"Dealer points : {computer_Points} ")

  # Does user or computer have a blackJack ?

blackJack(user,computer)
  

  # Is user's score over 21
  
pointsCheckerStart(player_Points,computer_Points)
  
  # Ask the user if he want's to get another card


while should_continue :
  # player Turn
  answerOf = input("would you like to get another card ? y/n ") 

  if answerOf == yes:
    player_Points = giveAnotherCard("Player",user,player_Points)
    if player_Points > 21:
      print(f"Player's points : {player_Points} \n")
      print("end of the game")
      print("You loose")
      should_continue = False 
    should_continue
      
# dealer Turn
  elif answerOf == no and computer_Points < 17:
    computer_Points = computer_play("Dealer",computer,computer_Points)
    final_Point_Checker(player_Points,computer_Points)
    should_continue


# End Of The party
  else:
    print(f"Player's hand: {user}")
    print(f"Player points : {player_Points}")
    final_Point_Checker(player_Points,computer_Points)
    should_continue = False
    
    
# -----  Angela solution ----------

############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
import random
from replit import clear
from art import logo

def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.
def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""

  #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user_score, computer_score):
  #Bug fix. If you and the computer are both over, you lose.
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"


  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def play_game():

  print(logo)

  #Hint 5: Deal the user and computer 2 cards each using deal_card()
  user_cards = []
  computer_cards = []
  is_game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

  while not is_game_over:
    #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True

  #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()
