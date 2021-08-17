def prime_checker(number): 
  if (number == 1) or (number == 2): 
    if number == 2: 
      print("It's a prime number.") 
    else: 
      print("It's not a prime number.") 
    
  elif number > 2: 
    x = 2 

    while number >= x: 
      remains = number % x 

      if number == x: 
        print("It's a prime number.") 
        break 

      elif remains == 0: 
        print("It's not a prime number.") 
        break 

      else: 
        x += 1 
