
# calculator

def add(n1,n2):
  return n1 + n2


def substract(n1,n2):
  return n1 - n2


def multiply(n1,n2):
  return n1 * n2


def divide(n1,n2):
  return n1 / n2


operations = {
  "+":add , 
  "-":substract,
  "*":multiply,
  "/":divide
  }

num1 = int(input("What's the first number ? : "))



for symbol in operations:
  print(symbol)


operation_symbol = input("Pick an operation from the line above: ")

num2 = int(input("What's the second number ? : "))

operation_process = operations[operation_symbol](num1,num2)

# solution N°2: calculation_function =  operations[operation_symbol]

# => answer = calculation_function(num1,num2)
# => calculate a result from the preview's result 

print(f"{num1}{operation_symbol}{num2} = {operation_process}")

operation_symbol = input("pick another operation: ")
num3 = int(input("what's the next number?: "))

calculation_function = operations[operation_symbol]
second_answer = calculation_function(calculation_function(num1,num2),num3)
print(f"{num1}{operation_symbol}{num2} = {second_answer}")

