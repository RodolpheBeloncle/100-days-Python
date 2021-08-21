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

num2 = int(input("What's the second number ? : "))

for symbol in operations:
  print(symbol)


operation_symbol = input("Pick an operation from the line above: ")

operation_process = operations[operation_symbol](num1,num2)

print(operation_process)
