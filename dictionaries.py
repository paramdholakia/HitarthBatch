"""

1 : Rahul Sharma
2 : Jaydeep Verma
3 : Harsh Shah
4 : Tirth Solanki
5 : Rudra Soni
6 : Harsha Thakkar
7 : Priya gohil

# Dictionaries are type of Data which is used to store data in key value pairformat.
# It is mutable and ordered collection of data. 
# It is defined by using curly braces {}.

# IN PYTHON VERSION 3.6 AND BEFORE THE DICTIONARIES WERE UNORDERED COLLECTION OF DATA 
# BUT IN PYTHON VERSION 3.7 AND AFTER THE DICTIONARIES ARE ORDERED COLLECTION OF DATA.
 
{
    key : value,
    key : value,
    key : value,
    key : value
}

{1,2,3} # SET 
"""

# studentData = {
# keyValues : DataValues
#         1 : "Rahul Sharma",
#         2 : "Jaydeep Verma",
#         3 : "Harsh Shah",
#         4 : "Tirth Solanki",
#         5 : "Rudra Soni",
#         6 : "Harsha Thakkar",
#         7 : "Priya gohil"
# }
# print(studentData)
# print(type(studentData))

# ------------------------------------------------------------------
# How to retrieve data from dictionary using key values.
# print(studentData[5])
# print(studentData[12554])

# get() method is used to retrieve data from dictionary using key values.
# print(studentData.get(2))
# print(studentData.get(24))

# print(studentData.get(24, "STUDENT DATA DOESN'T EXIST"))
# print(studentData.get(4, "STUDENT DATA DOESN'T EXIST"))

# ------------------------------------------------------------------

# carDetails = {
#     "Name"  : "Maruti",
#     "Model" : "Swift",
#     "Color" : "Red",
#     "Price" : 800000,
#     "Year"  : 2022,
#     "Owner" : 1
# }

# keys() method is used to retrieve all the keys from dictionary.
# it provides a set like object 
# print(carDetails.keys())

# values() method is used to retrieve all the values from dictionary.
# print(carDetails.values())
# ------------------------------------------------------------------
# product = {
#     "type" : "Mobile",
#     "brand" : "Apple",
#     "name" : "Iphone 17",
#     "model" : "Pro Max",
#     "color" : "Black",
#     "price" : 170000,
# }

# Changing the key value pair using square brackets.
# product["color"] = "Orange"

# Adding the new key value pair using square brackets.
# product["operating system"] = "IPhone OS26"

# update() method is used to update the key value pair in dictionary. 
# and it is also used to add new key value pair in dictionary.


# product.update(
#     {
#         "color" : "White",
#         "OS" : "IPhone OS26"
#     }
# )

# ------------------------------------------------------------------

studentData = {
        1 : "Rahul Sharma",
        2 : "Jaydeep Verma",
        3 : "Harsh Shah",
        4 : "Tirth Solanki",
        5 : "Rudra Soni",
        6 : "Harsha Thakkar",
        7 : "Priya gohil"
}
# For removal in Dictionaries we have 2 Methods and 1 Keyword

# 1. pop() method : it is used to remove a key-value pair
# from the dictionary based on the specified key.
# if you don't specify a default value and the key is not found, it raises a KeyError.
# if you specify a default value and the key is not found, it returns the default value instead of raising an error.
# pop method returns the value associated with the specified key if it exists, and removes the key-value pair from the dictionary.

# print(studentData)

# student_name = studentData.pop(1)
# print(student_name)
# message = studentData.pop(1, "STUDENT DATA DOESN'T EXIST")
# print(message)

# print(studentData)


# 2. popitem() method : it is used to remove and return an arbitrary key-value pair from the dictionary.
# It removes the last inserted key-value pair in Python 3.7 and later versions,
# but in earlier versions, it removes an arbitrary key-value pair.
# print(studentData.popitem())


# del keyword : it is used to delete a key-value pair from the dictionary based on the specified key.

# del studentData[4]
