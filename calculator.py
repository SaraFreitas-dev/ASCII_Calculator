from img.ascii import calculator_draw, calculator_text, bye

def sum(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operations = {
    "+": sum,
    "-": subtract,
    "*": multiply,
    "/": divide,
}



def calculator():
    end_calculator = False

    while not end_calculator:
        print(calculator_text)
        print("\nWelcome to Our Vintage Calculator ! \n")

        num1 = float(input("What's the first number? "))
        num2 = float(input("What's the next number? "))

        

        continue_calculation = True

        while continue_calculation:
            for symbol in operations:
                print(symbol)
            choose_operation = input("Pick an operation from the line above: ")
            

            if choose_operation in operations:
                operation_function = operations[choose_operation]
                result = operation_function(num1, num2)
                print(f"\n{calculator_draw}")
                print(f"{num1} {choose_operation} {num2} = {result}")
                
                next_step = input(f"\nType 'y' to continue calculating with {result}, 's' to start a new calculation, or 'e' to exit: ").lower()
                if next_step == 'y':
                    num1 = result
                    num2 = float(input(f"First number is {result} What's the next number? "))
                elif next_step == 's':
                    continue_calculation = False
                elif next_step == 'e':
                    print(bye)
                    continue_calculation = False
                    end_calculator = True
                else:
                    print("Invalid input. Exiting calculator.")
                    print(bye)
                    continue_calculation = False
                    end_calculator = True
            else:
                print("Invalid operation. Please choose a valid operation.")

calculator()
