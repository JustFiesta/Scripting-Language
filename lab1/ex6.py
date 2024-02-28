print("===== Calculator =====")

num1 = int(input("Input first num: "))
operation = input("Choose operation (+, -, *, /): ")
num2 = int(input("Input second num: "))


match operation:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)        
    case "*":
        print(num1 * num2)
    case "/":
        print(num1 / num2)
    case _:
        print("Choosed wrong operation!!!")
        