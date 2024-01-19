from calculator_art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
        
    continue_calculation = True
    while continue_calculation: 
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
    
        continue_calculation = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ")
        if continue_calculation == "y":
            num1 = answer
            continue_calculation = True
        else:
            continue_calculation = False
            calculator()

calculator()