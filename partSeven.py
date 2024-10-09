def main():
    while True:
        num1 = int(input("Input first number: "))
        num2 = int(input("Input second number: "))
        operation = input("Pick operation: (+, -, /, *, ^, or %), type 'quit' to cancel operation. ")

        if operation.lower()=="quit":
            print("Cancelling operation.")
    break 

# ????????

    else:
        match operation:
            case "+":
                result = (num1 + num2)
                print(f"{num1} + {num2} = {result}")
            case "-":
                result = (num1 - num2)
                print(f"{num1} - {num2} = {result}")
            case "/":
                if num2==0:
                    return("Error! Cannot divide by 0.")
                else:
                    result = (num1 / num2)
                    print(f"{num1} / {num2} = {result}")
            case "*":
                result = (num1 * num2)
                print(f"{num1} * {num2} = {result}")
            case "^":
                result = (num1 ** num2)
                print(f"{num1} ^ {num2} = {result}")
            case "%":
                if num2==0:
                    print ("Error! Cannot perform modulo by 0.")
                else:
                    result = (num1 % num2)
                    print(f"{num1} % {num2} = {result}")
            case _:
                print("Invalid")
                    
main()
            
