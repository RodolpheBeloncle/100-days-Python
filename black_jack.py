
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
anotherCard = True
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


  # user and dealer get 2 random cards
  
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

