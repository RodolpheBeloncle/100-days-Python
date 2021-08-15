
import random


# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")



# number of guest 

numberOfGuest = len(names)

# waiter's  random choice
waiter_choice_random_CreditCard = random.randint(0,numberOfGuest-1)

# attributing random index's number to the list name
randomName = names[waiter_choice_random_CreditCard]

print(f"{randomName} is going to buy the meal today!")
