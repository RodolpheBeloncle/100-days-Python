#Number Guessing Game Objectives:
from art import logo
import random
import re

# ----- Data game ----

number_to_find = random.randrange(0,100,1)
easyMode = 10
hardMode = 5
counter = 0
print(logo)


def number_checker(guess_A_Number,number_to_find,count):
  
  if guess_A_Number > number_to_find:
    print("Too high.")
    print(f"Turn remaining {count} ")
    return count
   
  elif guess_A_Number < number_to_find:
    print("Too low.")
    print(f"Turn remaining {count} ")
    return count
    
  elif  guess_A_Number == number_to_find:
    print("you found it !!!")
    print(f"the number was {number_to_find}")
    return False


# ------ Game --------
game_continue = True

level = input("Choose your level 'easy'/ 'hard' : ")

if level == "easy":
  counter = easyMode
    
elif level == "hard":
  counter = hardMode
  

while game_continue:
  
  guess_A_Number = int(input("Guess a number between 0 and 100 : "))

  counter -= 1

  number_checker(guess_A_Number,number_to_find,counter)

  

  if counter == 0 or guess_A_Number == number_to_find:
    print("You loose the game")
    game_continue = False
#---- angela's solution --------

