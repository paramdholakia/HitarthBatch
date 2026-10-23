list1 = [1, 2, 3, 4, 5]

# print("Original list:", list1)

# ------------------------------
# Append method
# The append() method adds element to the end of a list.

# list1.append(6)
# print("After append:", list1)

# ------------------------------
# Insert method
# The insert() method inserts an element at a specified position in the list.

# list1.insert(3, 4)
# print("After insert:", list1)

# ------------------------------
# Extend Method
# It adds the List elements to the end of the current list.
# list2 = [6, 7, 8, 9, 10]

# list1.extend(list2)
# print("After extend:", list1)

# ------------------------------------------------------------------------------------------

# ------------------------------
# pop method
# The pop() method removes the element at the specified position in the list, and returns it.
# If no index is specified, the pop() method removes and returns the last item in the list.

# print(list1)
# list1.pop()
# print(list1)
# list1.pop(1)
# print(list1) 



# ------------------------------
# Remove method
# Remove method removes the first matching element (which is passed as an argument) from the list.

# list1.append(4)

# print(list1)
# list1.remove(4)
# list1.remove(4)
# print(list1)

# ------------------------------
# Clear method
# The clear() method removes all items from the list.

# print(list1)
# list1.clear()
# print(list1)





# ------------------------------
# Copy Method
# The copy() method returns a shallow copy of the list.

# list2 = list1.copy()
# print("Original list:", list1)
# print("Copied list:", list2)

# ------------------------------
# index method
# The index() method returns the index of the first matching element in the list.

# fruits = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon', 'mango']
# print(fruits.index('fig'))

# ------------------------------
# reverse method
# The reverse() method reverses the elements of the list in place.

# print(list1)
# list1.reverse()
# print(list1)


# ------------------------------
# sort method
# The sort() method sorts the elements of the list in ascending order by default.
# To sort the elements in Ascending order, you can use the reverse parameter and set it to False.
# To sort the elements in Descending order, you can use the reverse parameter and set it to True.

# list2 = [5, 2, 9, 1, 5, 6, 3, 4, 6, 7]
# print("Original list:", list2)
# list2.sort(reverse=True)
# print("Sorted list:", list2)


# ------------------------------
# count method
# The count() method returns the number of times a specified element appears in the list.

# numbers = [10, 20, 10, 30, 10, 40]
# print(numbers.count(10))

# ------------------------------
# len() method !IMPORTANT! | IT IS A BUILT IN METHOD NOT A LIST METHOD
# The len() method returns the number of items in a list.

# list1 = [10, 20, 30, 40, 50]
# print(len(list1))

# ------------------------------
# max() method | IT IS A BUILT IN METHOD NOT A LIST METHOD
# The max() method returns the largest item in a list.
# fruits = ['a', 'aa', 'aba', 'ab']
# print(max(fruits))

# numbers = [10, 20, 30, 40, 50]
# print(max(numbers))

# ------------------------------
# min() method | IT IS A BUILT IN METHOD NOT A LIST METHOD
# The min() method returns the smallest item in a list.

# numbers = [10, 20, 30, 40, 50]
# print(min(numbers))


# ------------------------------
# sum() method | IT IS A BUILT IN METHOD NOT A LIST METHOD
# The sum() method returns the sum of all items in a list.

numbers = [10, 20, 30, 40, 50, 50]  
print(sum(numbers))

marks = [47, 48, 49, 50, 20]

print(sum(marks)/len(marks))  # Average of the list
# ------------------------------