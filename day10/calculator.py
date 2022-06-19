from art2 import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}

def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for operator in operations:
        print(operator)


    flag = True
    while flag:
        symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calc = operations[symbol]  #this is just pointing to the symbol function
        answer = calc(num1,num2)
        print(f"{num1} {symbol} {num2} = {answer}")

        contd = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation. ")
        if contd == 'y':
            num1=answer
        elif contd == 'n':
            flag= False
            calculator()
        else:
            print("You entered an invalid option. Try again!")

calculator()