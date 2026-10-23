while True:
    print("===================")
    print("Welcome to Calculator")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Floor Division (//)")
    print("6. Power (**)")
    print("7. Modulo (%)")
    print("9. Exit : Type '-1' : ")
    print("===================")
    userChoice = input("\nSelect Your Operation : ")
    print("===================")

    if userChoice == "-1":
        print("\nThank you for using Calculator!!\n")
        break

    if userChoice not in ("+", "-", "*", "/", "//", "**", "%"):
        print("You have entered Wrong Option")
        continue

    number1 = float(input("Enter Number 1 : "))
    number2 = float(input("Enter Number 2 : "))

    if number2 == 0 and userChoice == "/":
        print("YOU CANNOT DIVIDE WITH ZERO!!")
        continue

    match userChoice:
        case "+":
            print(number1 + number2)   
        case "-":
            print(number1 - number2)
        case "*":
            print(number1 * number2)
        case "/":
            print(number1 / number2)
        case "//":
            print(number1 // number2)
        case "**":
            print(number1 ** number2)
        case "%": 
            print(number1 % number2)
    print("\n")
