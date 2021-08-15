# My solution

import random

# Created hangman part:

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


#-----------------------

word_list = ["aardvark", "baboon", "camel"]

# random choosen word in the list
chosen_word = random.choice(word_list)

# stringified choosen word (nice & neat)
stringified_chosen_word = "".join(chosen_word)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')


#Create blanks word

display = []
for _ in range(word_length):
    display += "_"




#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.



# counter shot
counter = 0
hangPoint = 0

# Loop while 2 words are not egual:
while display is not chosen_word:

  # stringified builded display word (nice & neat)
  stringified_Display = "".join(display)
  print(stringified_Display )
  

  # Condition to loop(continue):
  if stringified_Display != stringified_chosen_word:

  # ask a letter?:
    guess = input("Guess a letter: ").lower()
    counter += 1

  
    # adding the guess letter if == letter form chosen_word:
    for position in range(word_length):
      
      letter = chosen_word[position]
      
      print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
      
        
      if letter == guess:
        print("right letter")
        display[position] = letter
        guess

      
          
  # Condition to break the loop
  elif stringified_Display == stringified_chosen_word:

    print(f'''
    !! you found the word in {counter} shots!! well done
    ''')
    print(stringified_Display )
    print(stringified_chosen_word)
    break


    
    
    
      


    

