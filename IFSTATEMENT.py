temp = int(input("Enter a temperature in Celsius: "))


if temp > 30:
    print("HOT")
else:
    if temp > 20:
        print("WARM")
        if temp > 10:
            print("COOL")
    else:
        print("COLD")