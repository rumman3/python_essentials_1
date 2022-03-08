def addition(number1, number2):
    return number1 + number2


def subtraction(number1, number2):
    return number1 - number2


def multiplication(number1, number2):
    return number1 * number2


def division(number1, number2):
    try:
        return number1 / number2
    except ZeroDivisionError:
        return "Error"


def read_number(number_option):
    while True:
        number_str = input(f"Please Enter {number_option}: ")
        if number_str.isdigit():
            number = int(number_str)
            return number
        else:
            print("The number should contain only digits")


def read_operator():
    valid_operators = ["+", "-", "/", "*", "Q", "q"]
    while True:
        operator_str = input(f"Please Enter Operator or Type 'Q' to quit: ")
        if operator_str in valid_operators:
            return operator_str
        else:
            print("Please Enter a Valid Operator from the following: +  -  /  *")


if __name__ == '__main__':

    number1 = read_number("a number")
    number2 = read_number("another number")
    while True:
        operator = read_operator()

        if operator == "+":
            result = addition(number1, number2)
        if operator == "-":
            result = subtraction(number1, number2)
        if operator == "/":
            result = division(number1, number2)
        if operator == "*":
            result = multiplication(number1, number2)
        if operator.upper() == "Q":
            break
        print(f"{number1} {operator} {number2} = {result}")
        if result == "Error":
            print("Zero Division Error, Type a different operator")