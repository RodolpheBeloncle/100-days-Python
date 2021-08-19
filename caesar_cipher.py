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
  
    #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text, shift_amount):
  #TODO-2: Inside the encrypt function, shift each letter of the text forwards in the alphabet by the shift amount and print the encrypted text.  
  #e.g. 
  #plain_text = "hello"
  #shift = 5
  #cipher_text = "mjqqt"
  #print output: "The encoded text is mjqqt"
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    new_letter = alphabet[new_position]
    cipher_text += new_letter
  print(f"The encoded text is {cipher_text}")

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
encrypt(plain_text=text, shift_amount=shift)


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
