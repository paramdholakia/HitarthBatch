""" 
nested ifs : it means if statements inside if statements


What is nested loop

When we write loops insde another loop, we call it nested loop
"""

# for i in range(1, 4): # 1, 2, 3
#     for j in range(1, 4): # 1, 2, 3
#         print(i, j)
    

""" 
for i in range(1,4) : 1, 2, 3

i = 1
    j = 1 (1 1)
    j = 2 (1 2)
    j = 3 (1 3)

i = 2
    j = 1 (2 1)
    j = 2 (2 2)
    j = 3 (2 3)

i = 3
    j = 1 (3 1)
    j = 2 (3 2)
    j = 3 (3 3)
"""


""" 
* * * 
* * *  
* * * 
"""
# for i in range(3):
#     for j in range(5):
#         print("*", end=" ")
#     print()

# for i in range(3):
#     for j in range(3):
#         print("*", end=" ") # * * *
#     print()



# for i in range(5):
#     for j in range(i+1):
#         print("*", end="")
#     print()

"""
Dry Run : 

for i in range(3) : 0, 1, 2

i = 0
    for j in range(1) : 0
    j = 0

i = 1
    for j in range(2) : 0, 1
    j = 0
    j = 1

i = 2
    for j in range(3): 0, 1, 2
    j = 0
    j = 1
    j = 2

Output :
*
**
***
"""


# for i in range(1, 4):
#     for j in range(1, 7):
#         print("Hello")

# How many times will this loop run?
# i = 1, 2, 3       | 3 Times
# j = 1,2,3,4,5,6   | 6 Times
# 6 + 6 + 6 = 18 Times


# for row in range(5):
#     for column in range(row*2):
#         print(f"Row {row}, column {column}")

""" 
row : 0, 1, 2, 3, 4

row = 0
    column = 0
    # End
# End

row = 1
    column = 0, 1
    # 2 Times

row = 2
    column = 0, 1, 2, 3
    # 4 Times

row = 3
    column = 0, 1, 2, 3, 4, 5
    # 6 Times

row = 4
    column = 0, 1, 2, 3, 4, 5, 6, 7
    # 8 Times

# 2 + 4 + 6 + 8 
"""




""" 
*****
****
***
**
*
"""
# n = int(input("Enter a number : "))
# for i in range(n, 0, -1):
#     for j in range(i):
#         print("*",end="")
#     print()

""" 
    * # i = 1, j = 1
   ** # i = 2, j = 1, 2
  *** # i = 3, j = 1, 2, 3
 **** # i = 4, j = 1, 2, 3, 4
*****
"""
# n = int(input("Enter a number : "))
# for i in range(1, n+1):
#     print(" " * (n-i) , end="")
#     for j in range(1, i+1):
#         print("*", end="")
#     print()

"""
5
i  " " * (n-i)      j loop
1   5-1= 4 Times    1 -> *
2   5-2= 3 Times    1,2 -> **
3   5-3= 2 Times    1,2,3 -> ***
4   5-4= 1 Time     1,2,3,4 -> ****
5   5-5= 0 Time     1,2,3,4,5 -> *****
"""



""" 
*****
 ****
  ***
   **
    *
"""
# n = int(input("Enter a number : "))
# for i in range(5, 0, -1):
#     print(" " * (n-i), end="")
#     for j in range(i):
#         print("*",end="")
#     print()

""" 
* * * * *
  * * * *
    * * *
      * *
        *
"""
# n = int(input("Enter a number : "))
# for i in range(5, 0, -1):
#     print(" " * (n-i)*2, end="")
#     for j in range(i):
#         print("* ",end="")
#     print()

"""
    *
   * *
  * * *
 * * * *
* * * * *
"""

# for i in range(5):
#     print(" "* (4-i), end="")
#     for j in range(i+1):
#         print("*", end=" ")
#     print()

"""
* * * * *
 * * * *
  * * *
   * *
    *
"""

# n = int(input("Enter a number : "))
# for i in range(n, 0, -1):
#     print(" "* (n-i), end="")
#     for j in range(i):
#         print("*", end=" ")
#     print()

"""
    *
   * *
  * * *
 * * * *
* * * * *
 * * * *
  * * *
   * *
    *
"""
# n=int(input("enter number:"))

# for i in range(n):
#     print(" " * (n-i-1), end="")
#     for j in range(i+1):
#         print("*", end=" ")
#     print()

# for i in range(n-1, 0, -1):
#     print(" " * (n - i), end="")

#     for j in range(i):
#         print("*", end=" ")
#     print()


"""
* * * * *
*       *
*       *
*       *
* * * * *
"""
# n = int(input("Enter a number : "))
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n-1 or j == 0 or j == n-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

""" 
* * * * * * * * * *
*                 *
*                 *
* * * * * * * * * *

n and m
"""
# n = int(input("Enter Length : "))
# m = int(input("Enter Width : "))

# for i in range(n):
#     for j in range(m):
#         if i == 0 or i == n-1 or j == 0 or j == m-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

""" 
*
* *
*   *
*     *
* * * * *
"""
# n = int(input("Enter a number : "))
# for i in range(n):
#     for j in range(n):
#         if j == i or j == 0 or i == n-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

""" 
    *
   * *
  *   *
 *     *
* * * * *
"""

# n = int(input("Enter a number : "))

# for i in range(1, n + 1): # 1 to n
#     print(" " * (n - i), end="")

#     for j in range(1, i + 1):
#         if j == 1 or j == i or i == n:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")

#     print()

# for i in range(n, 0, -1): # n to 1
#     print(" "*(n-i), end="")
#     for j in range(1, i+1):
#         if j == i or j == 1 or i == n:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

""" 
    * 
   * * 
  *   * 
 *     * 
*       * 
 *     * 
  *   * 
   * * 
    * 

"""

# n = int(input("Enter a number : "))

# for i in range(1, n + 1): # 1 to n
#     print(" " * (n - i), end="")

#     for j in range(1, i + 1):
#         if j == 1 or j == i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")

#     print()
# for i in range(n-1, 0, -1): 
#     print(" " * (n - i), end="")

#     for j in range(1, i + 1):
#         if j == 1 or j == i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")

#     print()

# ------------------------------------

# list1 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# for i in range(3): # 0, 1, 2
#     for j in range(3): # 0, 1, 2
#         print("Item :", list1[i][j])

# for i in range(3):
#     for j in range(3):
#         print(list1[i][j], end=" ")
#     print()

""" 
1 2 3
4 5 6
7 8 9
"""

"""
Item : 1
Item : 2
Item : 3
Item : 4
....
Item : 9
"""