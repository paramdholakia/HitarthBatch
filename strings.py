# Hello world

#  Single line strings
# firstName = "Raju hasdjkshd"
# lastName = 'Kumar'

# print(firstName)
# print(lastName)

# print(type(firstName))
# print(type(lastName))

# # Multi line strings
# sentence = """This 
# is 
# a 
# multi 
# line 
# string
# """

# var = '''This 
# is 
# a 
# multi 
# line 
# string'''

# print(sentence)
# print(var)

# print(type(sentence))
# print(type(var))

# indexing in strings
# name = "Raju Shrivastava"
# print(name)
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])

# print(name[-1])
# print(name[-2])
# print(name[-3])
# print(name[-4])


# string slicing
# variable[start_index(0):ending_index(n-1):step(1)]
# print(name[0:4])
# print(name[5:])


firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")

# print("Hello ", firstName, lastName, ", welcome to my python program")
# print("Hello " + firstName + " " + lastName + ", welcome to my python program")

# formatted strings 
print(f"Hello , {firstName}, {lastName}, welcome to my python program")
print("Hello , {}, {}, welcome to my python program".format(firstName, lastName))