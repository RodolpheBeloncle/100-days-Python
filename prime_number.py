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
        
# Angela's solution :

  def prime_checker(number):
    is_prime = True
    
    for i in range(2,number):
      if number % i == 0:
        is_prime = False
      if is_prime:
        # if it's clearly divisible with remains 0 
        print("It's a prime number")
      else:
        print("It's not a prime number")
      
