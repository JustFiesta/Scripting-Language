import math

print("===== Calculator =====")

num1 = int(input("Input first num: "))
operation = input("Choose operation (+, -, *, /, c - circle circumference, f - circle field, q - quadratic equasion (num1*x^2, num1*x, c)): ")
num2 = int(input("Input second num: "))


def add(num1, num2):
    
    result = num1 + num2
    save_to_history(result)

    return result

def substract(num1, num2):

    result = num1 - num2
    save_to_history(result)

    return result

def multiply(num1, num2):
    result = num1 * num2
    save_to_history(result)

    return result

def divide(num1, num2):
    result = num1 / num2
    save_to_history(result)

    return result

def field(num1):

    result = math.pi *  (num1**2)
    save_to_history(result)

    return result

def circut(num1):
    result = 2 * math.pi * num1
    save_to_history(result)

    return result

def save_to_history(result):
    file = open("results.txt", "a")

    file.write( str(result) + "\n")
    
    file.close

def quadratic_equasion(a, b, c):
    

    delta = (b**2) - 4 * a * c

    if delta > 0:
        x1 = (-b - math.sqrt(delta))/2 * a
        x2 = (-b + math.sqrt(delta))/2 * a
    
        save_to_history(x1)
        save_to_history(x2)
    elif delta == 0:
        x0 = -(b/(2*a))
        save_to_history(x0)
    else:
        print("No results for delta < 0")
        save_to_history("No results for delta < 0")


match operation:
    case "+":
        print(add(num1, num2))
    case "-":
        print(substract(num1, num2))        
    case "*":
        print(multiply(num1, num2))
    case "/":
        print(divide(num1, num2))
    case "f":
        print(field(num1))
    case "c":
        print(circut(num1))
    case "q":
        num3 = int(input("Provide parameter - c: "))
        print(quadratic_equasion(num1, num2, num3))
    case _:
        print("Choosed wrong operation!!!")
        