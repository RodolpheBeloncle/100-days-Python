
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


# first solution

while True:

  # list of possibilities
  choices = [rock,paper,scissors]

  # Player choice
  start_battle = int(input('''
  What do you choose ? :
  Type O for Rock
  Type 1 for Paper
  Type 2 for Scissors
  '''))

  if start_battle > len(choices)-1 :
    print("You have to choose a number between 0 and 2 nothing else !!")
    start_battle

  # numbers choosen of each player
  playerNumber = start_battle

  computerNumber =  random.randint(0,2)
  
  # player hand
  player_Choice = choices[int(start_battle)]
  print( player_Choice)

  # computer hand
  computer_Choice = choices[computerNumber]
  print(computer_Choice)

  # conditions to win

  

  if playerNumber == 0  and computerNumber == 2:
    print("You win !!")
    start_battle

  elif playerNumber == 2 and computerNumber == 1:
    print("You win !!")
    start_battle


  elif playerNumber == 1 and computerNumber == 0:
    print("You win !!")
    start_battle

  elif playerNumber == computerNumber:
    print("It's a draw!!")
    start_battle
    
  else:
    print("You loose!!")
    break

  

