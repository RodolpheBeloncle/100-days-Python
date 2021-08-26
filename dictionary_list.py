student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
#Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to covert scores into grades.👇
for student in student_scores:
  score = student_scores[student]
  if score > 90:
    student_grades[student] = "Outstanding"
  elif score > 80:
    student_grades[student] = "Exceeds Expectations"
  elif score > 70:
    student_grades[student] = "Acceptable"
  else:
    student_grades[student] = "Fail"
    

#Don't change the code below 👇
print(student_grades)



# --------- Exemple nesting Dictionnary list ---------------

##Python Dictionaries

programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again.",
}

#Retrieving items from dictionary.
# print(programming_dictionary["Function"])

#Adding new items to dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again."

#Create an empty dictionary.
empty_dictionary = {}

#Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

#Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary)

#Loop through a dictionary
# for key in programming_dictionary:
#   print(key)
#   print(programming_dictionary[key])

#######################################

#Nesting 
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

#Nesting a List in a Dictionary

travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Nesting Dictionary in a Dictionary

travel_log = {
  "France": 
  {"cities_visited": ["Paris", "Lille", "Dijon"], 
   "total_visits": 12},
  
  "Germany": 
  {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
   "total_visits": 5},
}

#Nesting Dictionaries in Lists

travel_log = [
{
  "country": "France", 
  "cities_visited": ["Paris", "Lille", "Dijon"], 
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]
# Add dictionnary with list in nested list:

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(countryVisited,TimesVisited,visitedCities):

  myNewList = {}

  myNewList["country"] = countryVisited
  myNewList["visits"] = TimesVisited
  myNewList["cities"] = visitedCities

  travel_log.append(myNewList)
  for key in myNewList:
    print(key)
    print(myNewList[key])
    
    
    add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

# exemple with higher_lower game

from art import *
from game_data import data
import random




nameList = []
nbFollower = []
descriptionList = []
countryList = []
count = 0

for key in data:
 nameList.append(key["name"])
 nbFollower.append(key["follower_count"])
 descriptionList.append(key["description"])
 countryList.append(key["country"])


def compareFunc(nameA,valA,nameB,valB):
  if valA < valB:
    answer = "B"
    return answer.lower()
  else:
    answer = "A"
    return answer.lower()


play = True

while play:
  random_choice1 = random.randrange(0,len(data))
  random_choice2 = random.randrange(0,len(data))

   
  VALUE_A = [nameList[random_choice1],descriptionList[random_choice1],countryList[random_choice1],nbFollower[random_choice1]] 

  VALUE_B = [nameList[random_choice2],descriptionList[random_choice2],countryList[random_choice2],nbFollower[random_choice2]]

  print(logo)

  print(f"Compare A : { VALUE_A[0]} , a { VALUE_A[1] } , from { VALUE_A[2] } ")
 
  print(vs)

  print(f"Against B : { VALUE_B[0] } , a { VALUE_B[1] } , from { VALUE_B[2] } ")

  question = input("who has more followers? type A or B : ").lower()
  

  if question == compareFunc(VALUE_A[0],VALUE_A[-1],{VALUE_B[0]},VALUE_B[-1]):
    count += 1
    print(f"You won 1 , Total points {count}")
    print(f"{VALUE_A[0]} a {VALUE_A[-1]} , {VALUE_B[0]} a {VALUE_B[-1]}")
    print("Continue")
    play = True
  else:
    print("you loose")
    print(f"{VALUE_A[0]} a {VALUE_A[-1]} , {VALUE_B[0]} a {VALUE_B[-1]}")
    print("end of the game")
    play = False
 
