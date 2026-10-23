""" 

Identity Operator
Identity operators are used to compare the memory locations of two objects. 
They check whether two variables point to the same object in memory.

is      : it checks if two variables point to the same object in memory 
          and returns True if they do, otherwise it returns False.    
is not  : it checks if two variables point to different objects in memory
          and returns True if they do, otherwise it returns False.    

"""


l1 = [1, 2, 3]
l2 = l1
l3 = [1, 2, 3]


# print(l1 is l2)
# print(l3 is l2)
# print(l1 is l3)


print(l1 is not l2)
print(l3 is not l2)
print(l1 is not l3)