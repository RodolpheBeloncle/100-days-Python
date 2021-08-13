def loveScore (firstName,secondName):

  firstName_to_Lower_Case = firstName.lower()
  secondName_to_Lower_Case = secondName.lower()

  concantenate_names = firstName_to_Lower_Case + secondName_to_Lower_Case

  t = concantenate_names.count("t")
  r = concantenate_names.count("r")
  u = concantenate_names.count("u")
  e = concantenate_names.count("e")

  wordTrueOccured = t + r + u + e
  print(wordTrueOccured)
  l = concantenate_names.count("l")
  o = concantenate_names.count("o")
  v = concantenate_names.count("v")
  e = concantenate_names.count("e")

  wordLoveOccured = l + o + v + e
  print(wordLoveOccured)

  stringifiedWordTrueOccured = str(wordTrueOccured)

  stringifiedWordLoveOccured = str(wordLoveOccured)

  addedStringifiedWords = stringifiedWordTrueOccured+ stringifiedWordLoveOccured 
  
  addedStringifiedWords_ToInt = int(addedStringifiedWords)
  print(f"true love occures {addedStringifiedWords_ToInt} times") 

  if addedStringifiedWords_ToInt < 10 or addedStringifiedWords_ToInt > 90:
    print(f"Your score is {addedStringifiedWords_ToInt}, you go together like coke and mentos.")

  elif addedStringifiedWords_ToInt > 40 and addedStringifiedWords_ToInt < 50:
    print(f"Your score is {addedStringifiedWords_ToInt}, you are alright together.")

  else:
    print(f"Your score is {addedStringifiedWords_ToInt}.") 


loveScore(name1,name2)
