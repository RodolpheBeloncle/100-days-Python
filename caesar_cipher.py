alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
alphabet_list_size = len(alphabet)-1

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

# ENCRYPT CODE

def encrypt(input_text,input_shift):

  # set input_text in the list
  encrypted_word = []

  # get each letter in the inputWord
  for letterWord in input_text:
    print(letterWord)

    # get letter's index in alphabet list
    for letter in alphabet:
      
      # compare and modifie letter
      if letter == letterWord:
        indexLetter = alphabet.index(letter)

        # encryption code 
        encrypt_code = indexLetter + input_shift

        if encrypt_code > alphabet_list_size:
         
          encrypt_code = 0 + (alphabet_list_size - indexLetter)

          encrypt_letter = alphabet[encrypt_code]

          encrypted_word.append(encrypt_letter)
         
          print(encrypt_code)

        elif encrypt_code < alphabet_list_size:

          encrypt_letter = alphabet[encrypt_code]

          encrypted_word.append(encrypt_letter)
         
          print(encrypt_code)
        #-----------------------------------------
    
  print(f"{''.join(encrypted_word)}")
  
  # DECRYPT CODE
  
  def decrypt(textInput,shiftInput):
  cipher_decrypt_text = ""

  for eachLetter in textInput:
    index = alphabet.index(eachLetter)
    new_Index = index - shiftInput
    cipher_decrypt_text += alphabet[new_Index]
   print(f"The decrypt text is {cipher_decrypt_text}")


  def test(choice):

    if choice == "encode":
      encrypt(plain_text=text, shift_amount=shift)

    elif choice == "decode":
     decrypt(text,shift)

  test(direction)
  
  
  # --------------- Angela's solution ------------------
  
  
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")

#TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
should_end = False
while not should_end:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
  #Try running the program and entering a shift number of 45.
  #Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
  #Hint: Think about how you can use the modulus (%).
  shift = shift % 26

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye")
    





# ---------- REFACTORING CODE ----------------


def caesar (inputText,shiftCode,choice):

  if choice == "decode":
    shiftCode *= - shiftCode

  crypted_text = ""
  for letter in inputText :
    position = alphabet.index(letter)
    new_position = position + shiftCode
    crypted_text += alphabet[new_position]
  print(f"The encoded text is {crypted_text}")


caesar(text,shift,direction)

# FINAL PROCESS WITH ERROR INPUT AND EXCEPTION

# ----- Process --------------------

continue_scripting = True

error_syntaxe = False

alphabet_size_list = len(alphabet)


while continue_scripting:


  def caesar(start_text, shift_amount, cipher_direction):

    end_text = ""

    if cipher_direction == "decode":
      shift_amount *= -1


    for char in start_text:

    # exceptions or error inpout :

      if char in alphabet == alphabet.index(" "):

        end_text += " "
        print("error input")
        continue
    
    
      elif char not in alphabet :
        end_text += char
        print("error input")
        continue
    
      # if shift amount > 26 (list size alphabet)

      if shift_amount > alphabet_size_list:

        position = alphabet.index(char)
        exception = alphabet_size_list % shift_amount
        end_text += alphabet[exception]

        new_position = alphabet[exception]


      elif shift_amount <= alphabet_size_list:
        position = alphabet.index(char)
        new_position = position + shift_amount
        end_text += alphabet[new_position]

    print(f"Here's the {cipher_direction}d result: {end_text}")


  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))



  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
 
  # while True restart or not 

  restart = input("restart the cipher program? yes/no : ")

  if restart == "no":
    continue_scripting = False
  elif restart == "yes":
    continue_scripting
  else :
    print("Type yes or no !!!!")
