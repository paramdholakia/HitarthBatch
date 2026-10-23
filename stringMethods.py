text = "HeLLo WoRld"
# print(text)

# --------------------------------------------------------------
# 1.> CASE CONVERSION METHODS
# --------------------------------------------------------------

# upper() method changes all the characters in a string to uppercase.
# print(text.upper())

# lower() method changes all the characters in a string to lowercase.
# print(text.lower())

# title() method changes the first character of each word to uppercase and the rest to lowercase.
# print(text.title())

# capitalize() method changes the first character of the string to uppercase and the rest to lowercase.
# print(text.capitalize())

# swapcase() method changes the case of each character in the string to its opposite case.
# print(text.swapcase())


# --------------------------------------------------------------
# 2.> removing spaces from a string
# --------------------------------------------------------------

# strip() method is used to remove any leading and trailing whitespace characters from a string.
# It does not remove spaces in between words.

# print("          hello world         ")
# print("          hello world         ".strip())

# lstrip() method is used to remove any leading whitespace characters from a string.
# print("          hello world         ".lstrip())

# rstrip() method is used to remove any trailing whitespace characters from a string.
# print("          hello world         ".rstrip())


# --------------------------------------------------------------
# 3.> Searching in a string
# --------------------------------------------------------------


# text = "Python Programming is fun. Python is easy to learn."

# find() method it returns the index of the first occurrence of a specified substring in a string.
# If the substring is not found, it returns -1.

# print(text.find("Python"))
# print(text.find("u"))
# print(text.find("Pro"))
# print(text.find("Java"))

# rfind() method it returns the index of the last occurrence of a specified substring in a string.
# print(text.rfind("Python"))


# index() method it returns the index of the first occurrence of a specified substring in a string.
# If the substring is not found, it raises a ValueError.
# print(text.index("Python"))
# print(text.index("u"))
# print(text.index("Pro"))
# print(text.index("Java")) # This line will raise a ValueError because "Java" is not found in the string.

# rindex() method it returns the index of the last occurrence of a specified substring in a string.
# print(text.rindex("Python"))


# count() method it returns the number of occurrences of a specified substring in a string.
# print("Python", text.count("Python"))
# print("a", text.count("a"))
# print("e", text.count("e"))
# print("i", text.count("i"))
# print("o", text.count("o"))
# print("u", text.count("u"))

# total_number = text.count("a") + text.count("e") + text.count("i") + text.count("o") + text.count("u")
# print("Total number of vowels in the string:", total_number)


# --------------------------------------------------------------
# 4.> Replacement in a string
# --------------------------------------------------------------

# replace() method is used to replace a specified substring with another substring in a string.

# text = "I Love Python, Python is great, i Enjoy Python Programming."
# print(text.replace("Python", "C++"))

# --------------------------------------------------------------
# 5.> Splitting and Joining a string
# --------------------------------------------------------------


# split() method is used to split a string into a list of substrings based on a specified delimiter/seperator.

# text = "I Love Python, Python is great, i Enjoy Python Programming."
# words = text.split()
# print(words)

# data = "1,Hiren,Thakkar,98,9456789123,hirent@gmail.com"

# sperated = data.split(sep=",")
# print(sperated)

# rsplit() method is used to split a string into a list of substrings based on a specified delimiter/seperator,
# starting from the right side of the string.

# seperated = data.rsplit(sep=",")
# print(seperated)

# splitlines() method is used to split a string into a list of lines based on the newline character (\n).

# text = """I love Pizza
# I love Mozzarella cheese
# and I love Paneer toppings on my pizza."""

# lines = text.splitlines()
# print(lines)

# join() method is used to join a list of strings into a single string, with a specified separator between each string.

# words = ("I", "Love", "Python", "Programming")
# str = " ".join(words)
# print(str)

# --------------------------------------------------------------
# 6.> Starts with and Ends with methods in string
# --------------------------------------------------------------
# str = "Python Programming is fun. Python is easy to learn."

# startswith() method is used to check if a string starts with a specified substring.

# print(str.startswith("P"))
# print(str.startswith("Python Pro"))
# print(str.startswith("abcd"))

# endswith() method is used to check if a string ends with a specified substring.

# print(str.endswith("arn."))
# print(str.endswith("Earn."))

# --------------------------------------------------------------
# 7.> Alignment methods in string
# --------------------------------------------------------------
str = "Python"

# center() method is used to center-align a string within a specified width, padding it with spaces on both sides by default.
#  if a different padding character is specified, it will be used instead of spaces.

# print(str.center(10))
# print(str.center(20, "-"))

# ljust() method is used to left-align a string within a specified width, padding it with spaces on the right side by default.
# print(str.ljust(10))
# print(str.ljust(10, "-"))


# rjust() method is used to right-align a string within a specified width, padding it with spaces on the left side by default.
# print(str.rjust(10))
# print(str.rjust(10, "-"))

# zfill() method is used to pad a string with zeros on the left side, up to a specified width.
# print(str.zfill(10))

# --------------------------------------------------------------
# 8.> Checking Content in string
# --------------------------------------------------------------

# isalpha() method is used to check if all the characters in a string are alphabetic (letters).
# print("Hello".isalpha())
# print("He11o".isalpha())
# print("Hello world".isalpha())

# isdigit()/isnumeric() method is used to check if all the characters in a string are digits (numbers).
# print("568923".isdigit())
# print("568 923".isdigit())
# print("568A923".isdigit())


# isalnum() method is used to check if all the characters in a string are alphanumeric (letters and numbers).
# print("Hello123".isalnum())
# print("Hello 123".isalnum())
# print("Hello💀123".isalnum())

# isspace(): Checks if all characters in the string are whitespace.
# print("   ".isspace())  # True
# print(" 12".isspace())  # False
# print("ab ".isspace())  # False

# islower(): Checks if all characters in the string are lowercase.
# print("hello".islower())  # True
# print("helLo".islower())  # False
# print("he llo".islower())  # True

# isupper(): Checks if all characters in the string are uppercase.
# print("HELLO".isupper())  # True
# print("HELlo".isupper())  # False
# print("HeLLo".isupper())  # False

# istitle(): Checks if the string is in title case (first letter of each word is uppercase).
# print("Hello World".istitle())  # True
# print("Hello world".istitle())  # False

# isascii(): Checks if all characters in the string are ASCII characters (0-127).
# print("Hello".isascii())  # True
# print("Hello🤝".isascii())  # False

# isidentifier(): Checks whether a string is a valid Python identifier/variable name.

# isprintable(): Checks if all characters in the string are printable.

# isdecimal(): Checks if all characters in the string are decimal characters.


# --------------------------------------------------------------
# 9.> Formatting in string
# --------------------------------------------------------------
# firstName = input("Enter your first name: ")
# lastName = input("Enter your last name: ")

# print("Hello ", firstName, lastName, ", welcome to my python program")
# print("Hello " + firstName + " " + lastName + ", welcome to my python program")

# formatted strings
# print(f"Hello , {firstName}, {lastName}, welcome to my python program")
# print("Hello , {}, {}, welcome to my python program".format(firstName, lastName))


# --------------------------------------------------------------
# 10.> Encoding in string
# --------------------------------------------------------------

# Python supports UTF-8 Format
# print("This is example of Encoding".encode("UTF-16"))


# --------------------------------------------------------------
# 11.> Translation in string
# --------------------------------------------------------------

# a -> 1
# b -> 2
# c -> 3
# d -> 4
# e -> 5

# maketrans(): Creates a translation mapping table for use with translate().

# table = "abcdef".maketrans("abcdef", "123456")

# translate(): Returns a string where some characters are replaced using the translation table.
# str = "Hello, I am learning Python programming. Python is fun and easy to learn."
# print(str.translate(table))

# --------------------------------------------------------------
# 12.> Partition in string
# --------------------------------------------------------------

# partition(): Splits the string at the first occurrence of a separator, returning a 3-tuple (before, separator, after).
# print("This was really fun".partition("was"))

# rpartition(): Splits the string at the last occurrence of a separator, returning a 3-tuple (before, separator, after).


# --------------------------------------------------------------
# 13.>  Prefix and Suffix string
# --------------------------------------------------------------

str = "Python Programming is fun. Python is easy to learn."

# removeprefix(): Removes a specified prefix string if present at the start.
print(str.removeprefix("Python Programming"))

# removesuffix(): Removes a specified suffix string if present at the end.
print(str.removesuffix("to learn."))

# --------------------------------------------------------------
# 14.>  Tabs in string
# --------------------------------------------------------------

# expandtabs(): Expands tab characters (\t) in a string to spaces, based on a specified tab size (default is 8).
print("Hello\tWorld".expandtabs(4))  


# --------------------------------------------------------------
# 15.>  Length of string
# --------------------------------------------------------------
str = "a     "

print(len(str))