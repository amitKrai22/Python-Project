# CALCULATOR
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def square(n1, n2):
    return n1 ** n2

operation = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
    "**":square
}
def calculator():
    num1 = float(input("what is the first number?: "))
    for symbol in operation:
        print(symbol)
    should_continue = True

    while should_continue:    
        operation_symbol = input("Pick an operation from above line. ")
        num2 = float(input("what is the next number?: "))
        calculate_operation = operation[operation_symbol]
        answer = calculate_operation(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        """operation_symbol = input("pick another symbol: ")
        num3 = int(input("what's the next number?: "))
        calculate_operation = operation[operation_symbol]
        second_answer = calculate_operation(first_answer, num3)

        print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")"""

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")== 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()            