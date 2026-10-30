"""
Functions : 
    Functions are Re-Usable block of code that performs specific Task

Always give function name, the task it does
    
Syntax : 

def function_name(parameters  {optional} ):
    # Reusable code
    # return value (optional)

# Calling a function
function_name(parameters {optional})

"""

# def greetingMessage():
#     print("Hello User!")
#     print("Welcome to Python Programming!")
#     print("I like pizza!")
#     print()


# greetingMessage()

# greetingMessage()

# greetingMessage()


"""
Define a function, that prints the table of 5
Call the function 5 times

    def multiplicationTable():
        for i in range(1, 11):
            print(f"5 X {i} = { 5 * i }")
        print("------------------------------")

But this function is limited to printing only Multiplication table of 5
We want that we can use this logic to get any Multiplication table

# Parameters
Parameters are variable limited to only function calls, that a function can accept data from

def func(variable1, variable2, ....):
    print(variable1)
    print(variable2)

func() # The function call like this will fail.. WHY? We have not provided any ARGUEMENTS

func(10, 20)
func(variable1 = 10, variable2 = 20)

Arguements are Data which are passed to the function whenever the function is called


"""
# def multiplicationTable():
#     for i in range(1, 11):
#         print(f"5 X {i} = { 5 * i }")
#     print("------------------------------")

# for i in range(5):
#     multiplicationTable()

# multiplicationTable()
# multiplicationTable()
# multiplicationTable()
# multiplicationTable()
# multiplicationTable()

def multiplicationTable(number):
    for i in range(1, 11):
        print(f"{number} X {i} = { number * i }")
    print("------------------------------")

multiplicationTable(number=5)
multiplicationTable(7)




"""
Enter Student Details, and print the student details in Following order
First Name : first_name  
Last Name : last_name
College Name : college_name
Marks : [marks1, marks2, marks3, marks4, marks5]
Total Marks : total_marks
Average Marks : average_marks

def printDetails(parameter(s)):
    # 

# INPUT BEFORE CALLING
printDetails(arguement(s))

"""



























































# n = int(input("Enter number of Total items : "))
# r = int(input("Enter number of Selected items : "))
# n_r = n - r 

# multiplier = 1
# for i in range(1, n+1):
#     multiplier *= i 
# n_fact = multiplier
# print(n, multiplier)

# multiplier = 1
# for i in range(1, r+1):
#     multiplier *= i 
# r_fact = multiplier
# print(r, multiplier)

# multiplier = 1
# for i in range(1, n_r+1):
#     multiplier *= i
# n_r_fact = multiplier 
# print(n_r, multiplier)


# print("Combinations : ", n_fact / (r_fact * n_r_fact) )