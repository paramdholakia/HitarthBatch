# ============================================================
#                ESCAPE SEQUENCES IN PYTHON
# ============================================================

# Escape sequences are special characters used inside strings.
#
# They start with a backslash (\) followed by another character.
#
# Example:
#
#     \n
#     ^^
#     |
#     Escape character
#
# The backslash tells Python:
# "The character after me has a special meaning."
#
# ============================================================
# 1. \n — NEW LINE
# ============================================================

# \n moves the following text to a new line.

print("Hello\nWorld")

# Output:
# Hello
# World


# You can use multiple \n:

print("Name: Alex\nAge: 20\nCity: Ahmedabad")

# Output:
# Name: Alex
# Age: 20
# City: Ahmedabad


# ============================================================
# 2. \t — TAB
# ============================================================

# \t inserts a horizontal tab.
# It is useful for creating spacing or simple tables.

print("Hello\tWorld")

# Output looks similar to:
# Hello   World


print("Name\tAge\tCity")
print("Alex\t20\tAhmedabad")
print("Rahul\t21\tMumbai")


# ============================================================
# 3. \b — BACKSPACE
# ============================================================

# \b moves the cursor one position backward.
#
# Depending on the terminal, the character before \b
# may appear to be removed/overwritten.

print("Hello\bWorld")

# Try experimenting with:
# print("Hello\b\bWorld")


# ============================================================
# 4. \' — SINGLE QUOTE
# ============================================================

# Normally, a single quote can be used to create a string:
#
#     'Hello'
#
# But what happens if we want an apostrophe inside it?

# This causes a problem:
#
# print('It's a beautiful day')
#
# Python thinks the string ends after:
#     'It'
#
# We can escape the apostrophe using \'

print('It\'s a beautiful day')

# Output:
# It's a beautiful day


# ============================================================
# 5. \" — DOUBLE QUOTE
# ============================================================

# The same idea works with double quotes.
#
# If the string itself uses double quotes, we can escape
# double quotes that need to appear INSIDE the string.

print("He said, \"Hello World\"")

# Output:
# He said, "Hello World"


# ============================================================
# 6. \\ — BACKSLASH
# ============================================================

# The backslash itself is an escape character.
#
# So if we simply write:
#
#     print("\")
#
# Python will produce an error.
#
# To print an actual backslash, we use TWO backslashes:
#
#     \\

print("This is a backslash: \\")

# Output:
# This is a backslash: \


# This is especially useful for Windows paths:

print("C:\\Users\\Alex\\Documents")

# Output:
# C:\Users\Alex\Documents


# ============================================================
# 7. \r — CARRIAGE RETURN
# ============================================================

# \r moves the cursor back to the beginning of the
# CURRENT line.
#
# Any text printed after \r may overwrite the text
# that was already there.

print("Hello\rWorld")

# You may see:
# World
#
# Why?
#
# "Hello" is printed first.
# \r moves the cursor back to the beginning.
# "World" is then printed over "Hello".


# Another example:

print("12345\rABC")

# The exact visual result can depend on your terminal.


# ============================================================
# 8. \f — FORM FEED
# ============================================================

# \f represents a form feed.
#
# Historically, a form feed was used by printers to move
# to the next page.
#
# Modern terminals may display it differently.

print("Hello\fWorld")

# The exact output can depend on the terminal/environment.
#
# This escape sequence is much less commonly used in
# normal Python programs.


# ============================================================
# 9. \ooo — OCTAL VALUE
# ============================================================

# \ooo represents a character using an OCTAL number.
#
# Octal = Base 8
#
# Octal digits are:
#
# 0 1 2 3 4 5 6 7
#
# Example:

print("\110\105\114\114\117")

# Output:
# HELLO
#
# Explanation:
#
# \110 = H
# \105 = E
# \114 = L
# \114 = L
# \117 = O


# ============================================================
# 10. \xhh — HEXADECIMAL VALUE
# ============================================================

# \xhh represents a character using a HEXADECIMAL number.
#
# Hexadecimal = Base 16
#
# Hexadecimal digits:
#
# 0 1 2 3 4 5 6 7 8 9 A B C D E F
#
# Example:

print("\x48\x45\x4C\x4C\x4F")

# Output:
# HELLO
#
# Explanation:
#
# \x48 = H
# \x45 = E
# \x4C = L
# \x4C = L
# \x4F = O


# ============================================================
#                 QUICK REFERENCE
# ============================================================

# Escape Sequence     Meaning
#
# \n                  New line
# \t                  Horizontal tab
# \b                  Backspace
# \'                  Single quote
# \"                  Double quote
# \\                  Backslash
# \r                  Carriage return
# \f                  Form feed
# \ooo                Octal character
# \xhh                Hexadecimal character


# ============================================================
#                 COMBINING ESCAPE SEQUENCES
# ============================================================

# Escape sequences can be combined in the same string.

print("===== STUDENT CARD =====\n")
print("Name:\tAlex")
print("Age:\t20")
print("City:\tAhmedabad")
print("Quote:\t\"Never stop learning!\"")
print("Folder:\tC:\\Python\\Projects")

# Output:
#
# ===== STUDENT CARD =====
#
# Name:   Alex
# Age:    20
# City:   Ahmedabad
# Quote:  "Never stop learning!"
# Folder: C:\Python\Projects


# ============================================================
# IMPORTANT IDEA
# ============================================================

# The BACKSLASH (\) is what makes an escape sequence special.
#
# For example:
#
#     print("Hello\nWorld")
#
# Python sees:
#
#     Hello
#     \n
#     World
#
# and interprets \n as:
#
#     "Move to the next line."
#
# So escape sequences allow us to control how strings
# are represented and displayed.