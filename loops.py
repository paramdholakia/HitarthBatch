""" 
Loops are used to execute a block of code repeatedly until a certain condition is met. 

In Python, there are two main types of loops: for loops and while loops.

Both for loops and while loops are entry controlled loops, 
meaning that the condition is checked before the loop body is executed.

# for loop

# syntax:

for iterable in sequence:
    # block of code to be executed


range() function is used to generate a sequence of numbers, which can be used in for loops.

range(start=0, stop, step=1)


range(1, 11) => 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 
                                           ^
                                           |
                                           i


"""

# for i in range(1, 11):
#     print("Hello World")

# for i in range(1, 11):
#     print(i, "Hello World")

# for var in range(10, 0, -1):
#     print(var, "Hello World")

# for i in range(1,101):
#     print(i, end=" ")

# Take 2 numbers from the user
# and print all the numbers between them

# num1=int(input("enter:"))
# num2=int(input("enter:"))
# for i in range(num1+1,num2):
#     print(i)


# Take 2 numbers from the user
# and print all the numbers between them
# if the number is even, print "even" instead of the number
# if the number is odd, print "odd" instead of the number

# num1=int(input("enter:"))
# num2=int(input("enter:"))
# for i in range(num1+1,num2):
#     if(i%2==0):
#         print(f"{i}even")
#     else:
#         print(f"{i}odd")

# num1=int(input("enter:"))
# num2=int(input("enter:"))
# for i in range(num1+1,num2):
#     if(i&1 == 0):
#         print(f"{i}even")
#     else:
#         print(f"{i}odd")


# sequence : list, string, dictionary, tuple, range

""" 
list1 = [1, 2, 3, 4, 5]
                     ^
                     | 
                     i
for i in list1:



str = "Hello"
           ^
           | 
           i

for i in str:


dict = {
    # key : value
    "Name" : "name",    
    "Number" : 123,     
    "Age" : 12
}




"""


# 1. Print numbers from 1 to 20.
# for i in range(1, 21):
#     print(i, end=" ")

# 2. Print all even numbers between 1 and 50.
# for i in range(1, 51):
#     if i % 2 == 0:
#         print(i, end = " ")

# 3. Print all odd numbers between 1 and 50.
# for i in range(1, 51):
#     if i % 2 != 0:
#         print(i, end = " ")

# 4. Print numbers from 20 down to 1.
# for i in range(20, 0, -1):
#     print(i, end=" ")

# 5. Print the first 10 multiples of 5.
# for i in range(1, 11):
#     print(5*i)

# 6. Find the sum of all numbers from 1 to 100.
# sum = 0
# for i in range(1, 101):
#     sum += i
# print(sum)


# 7. Find the sum of all even numbers between 1 and 100.

# sum = 0
# for i in range(1, 101):
#     if(i%2 == 0):
#         sum += i
# print(sum)

# 8. Count how many numbers between 1 and 100 are divisible by 3.
# count = 0
# for i in range(1, 101):
#     if i % 3 == 0:
#         count += 1
# print(count)


# 9. Take an integer from the user and find the sum of its digits.
#  123 = 1 + 2 + 3
#  50296 = 5 + 0 + 2 + 9 + 6

# number = int(input("Enter a number : "))
# sum = 0
""" 
    123   -> int
    "123" -> str
        ^
        |
        i
"""
# for i in str(number):
#     sum += int(i)
# print(sum)


# 10. Take an integer from the user and count the number of digits in it.
# number = int(input("Enter a number : "))
# count = 0
# for i in str(number):
#     count += 1

# print(count)

# 11. Take a number from the user and print its multiplication table from 1 to 10.
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

# number = int(input("Enter a number : "))
# for i in range(1, 11):
#     print(f"| {number} X {i} = {number * i} | ")


# 12. Take a base and exponent from the user and calculate the power using a for loop.
# 5^3 = 5 * 5 * 5

# base = int(input("Enter Base Value : "))
# power = int(input("Enter Power Value : "))
# temp = base

# for i in range(1, power):
#     temp = temp * base
# print(temp)

""" 
base = 5
power = 3

i : 1, 2, 3

i       temp        base        temp = temp * base
1       5           5           25
2       25          5           125
3       125         5           625
625
"""


# 13. Take a number from the user and calculate its factorial.
# 5! = 5 * 4 * 3 * 2 * 1
# n! = n * n-1 * n-2 * .... * 1
n = int(input("Enter a number : "))
temp = 1
for i in range(n, 0, -1):
    temp = temp * i
print(temp)

""" 
5! = 5 * 4 * 3 * 2 * 1
   = 20 * 3 * 2 * 1
   = 60 * 2 * 1
   = 120 * 1 = 120

i : 5  4  3  2  1

    temp   i    temp = temp * i
    1      5       5
    5      4       20
    20     3       60
    60     2       120
    120    1       120
"""



# 14. Take an integer from the user and find its largest digit.


n = int(input())
largest = 0

for i in str(n):
    if int(i) >= largest:
        largest = int(i)

print(largest)

""" 
n = 789
largest = 0
        n ->  "789"
                 i
    if 7 > 0 : largest = 7
    if 8 > 7 : largest = 8
    if 9 > 8 : largest = 9

print(largest) # 9
    
"""


# 15. Take an integer from the user and find its smallest digit.


# 16. Print all numbers between 1 and 100 that are divisible by both 3 and 5.


# 17. Take an integer from the user and count how many of its digits are odd and how many are even.


# 18. Take an integer from the user and reverse its digits.


# 19. Take an integer from the user and check whether it is a palindrome.


# 20. Take a three-digit number from the user and check whether it is an Armstrong number.

