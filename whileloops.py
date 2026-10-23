""" 
Loops are used for repeating a task/code 

for iterator in sequence:
    # code operation

While loops are our Condition based Entry Checked Loop that are used to execute 
a piece of code until a condition is False

# Syntax

while condition:
    # code operation
    # condition updation 
"""

# n = 1
# while n < 11:
#     print(n, end=" ")
#     n = n + 1

""" 
n = 1   n <= 5     print(n)    n += 1
  1     True        1           2
  2     True        2           3
  3     True        3           4
  4     True        4           5
  5     True        5           6
  6     False       X           X
"""

# n = 10
# while n > 0:
#     print(n, end=" ")
#     n = n - 1


# Take a Positive number from user, and print all the even numbers, 
# from negative of that number up until positive of that number
# using while loop

# n = int(input("Enter a POSITIVE number : "))
# while n < 0:
#     n = int(input("Enter a POSITIVE number : "))

# i = 0-n 
# while i <= n:
#     if i % 2 == 0:
#         print(i)
#     i += 1

# Take a number from the user and print its multiplication table from 1 to 10.
""" 
N x 1 = N*1
N x 2 = N*2
N x 3 = N*3
N x 4 = N*4
N x 5 = N*5
N x 6 = N*6
N x 7 = N*7
N x 8 = N*8
N x 9 = N*9
N x 10 = N*10
"""

# n=int(input("enter number:"))
# i=1
# while i<=10:
#     print(f"{n} X {i} = {n*i}")
#     i+=1


""" 
You are assigned to the application password checking, if user enters a wrong password
ask for the password again. until user puts in correct password, keep asking.
also print how many tries it took the user to enter the password

password = "ILovePizza"
"""

# userInput = input("Enter your Password : ")
# tries = 1
# secretPassword = "ILovePizza"
# while userInput != secretPassword:
#     userInput = input(f"Entered Wrong password {tries} time, Enter correct Password : ")
#     tries += 1

# print(f"LOGGED IN, YOU TRIED {tries} AMOUNT OF TIME")



""" 
We have to print all the digits in reverse from the integer input
using while loop only and maths


number = 12345
temp = 0

temp = (temp * 10) + number % 10
        0 + 5 = 5
temp =  5

number = number // 10
number = 1234


temp = (temp * 10) + number % 10
        50 + 4
temp =  54

number = number // 10
number = 123


temp = (temp * 10) + number % 10
        540 + 3
temp =  543

number = number // 10
number = 12


temp = (temp * 10) + number % 10
        5430 + 2
temp =  5432

number = number // 10
number = 1

temp = (temp * 10) + number % 10
        54320 + 1
temp =  54321

number = number // 10
number = 0.1    # number >= 1 # CONDITION IS WRONG


temp = 54321
num  = 12345
"""

# n = int(input("Enter a value : "))

# while n >= 1:
#     print(n % 10, end="")
#     n //= 10 # n = n // 10



# n = int(input("Enter a value : "))
# rev = 0
# copy_n = n 

# while n >= 1:
#     rev = (rev * 10) + (n % 10)
#     n //= 10 # n = n // 10

# if rev == copy_n:
#     print("Number is Palindrome")
# else:
#     print("Number is NOT Palindrome")


# Check whether the reverse of a number is greater than the original

# n = int(input("Enter a number : "))
# copy = n 
# reverse = 0

# while n >= 1:
#     reverse = (reverse * 10) + (n % 10)
#     n //= 10

# if copy == reverse:
#     print("Numbers are equal")
# elif copy > reverse:
#     print("original is bigger")
# else:
#     print("reverse is bigger")



# Add original number and its reverse
# n = int(input("Enter a number : "))
# copy = n 
# reverse = 0

# while n >= 1:
#     reverse = (reverse * 10) + (n % 10)
#     n //= 10
# print(f"Reverse {reverse} | Original {copy} = Sum {reverse + copy}")

# Count even digits and Count odd digits
# n = int(input("Enter a number : "))
# evenCount = 0
# oddCount = 0

# while n >= 1:
#     lastDigit = n%10

#     if lastDigit % 2 == 0:
#         evenCount += 1
#     else:
#         oddCount += 1

#     n//=10
# print(f"Even Count : {evenCount} \nOdd Count : {oddCount}")

# Sum of even digits and Odd digits Seperately
# n = int(input("Enter a number : "))
# evenSum = 0
# oddSum = 0

# copy_n = n

# while n >= 1:
#     lastDigit = n % 10
#     n //= 10

#     if lastDigit % 2 == 0:
#         evenSum += lastDigit
#     else:
#         oddSum += lastDigit

# print(f"Even Sum : {evenSum} and Odd Sum {oddSum}")

# product of even digits and Odd digits Seperately

# n = int(input("Enter a number : "))
# evenProduct = 1
# oddProduct = 1

# copy_n = n

# while n >= 1:
#     lastDigit = n % 10
#     n //= 10

#     if lastDigit % 2 == 0:
#         evenProduct *= lastDigit
#     else:
#         oddProduct *= lastDigit

# print(f"Even Product : {evenProduct} and Odd Product {oddProduct}")
    