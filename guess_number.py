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

from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"Pssst, the correct answer is {answer}") 

  turns = set_difficulty()
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")


game()

