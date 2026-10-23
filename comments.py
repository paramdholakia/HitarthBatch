# 1. Museum Entry
# A museum allows visitors only if they are 12 years or older.
# If they are allowed:
# If they are 60 or older, print "Senior Citizen Ticket"
# Otherwise print "Regular Ticket"
# If they are younger than 12, print "Entry Not Allowed"

age = int(input("Enter your age: "))

if age >= 12:
    if age >= 60:
        print("Senior Citizen Ticket")
    else:
        print("Regular Ticket")
else:
    print("Entry Not Allowed")




# ----------------------------------
# 2. Online Gaming Tournament
# A player can participate only if they are 16 years or older.
# If eligible:
# If they have played 100 or more matches, print "Qualified for Finals"
# Otherwise print "Practice More"
# Else print "Too Young to Participate"

age = int(input("Enter your age: "))

if age >= 16:
    matches = int(input("Enter the number of matches played: "))
    if matches >= 100:
        print("Qualified for Finals")
    else:
        print("Practice More")
else:
    print("Too Young to Participate")



# ----------------------------------
# 3. Laptop Purchase
# A customer can buy a gaming laptop only if their budget is ₹50,000 or more.

# If yes:
# If budget is ₹80,000 or more
# Print "Premium Gaming Laptop"
# Else
# Print "Mid-Range Gaming Laptop"
# Else print "Increase Budget"

budget = int(input("Enter your budget: "))

if budget >= 50000:
    if budget >= 80000:
        print("Premium Gaming Laptop")
    else:
        print("Mid-Range Gaming Laptop")
else:
    print("Increase Budget")

# ----------------------------------
# 4. College Library
# Students can borrow books only if they have a library card.
# Represent it as:
# 1 = Has Card
# 0 = Doesn't Have Card
# If they have a card:
# If pending fine is ₹0
# Print "Book Issued"
# Else
# Print "Pay Fine First"
# Else
# Print "Library Card Required"

library_card = int(input("Do you have a library card? (1 for Yes, 0 for No): "))

if library_card == 1:
    pending_fine = int(input("Enter pending fine amount: "))
    if pending_fine == 0:
        print("Book Issued")
    else:
        print("Pay Fine First")
else:
    print("Library Card Required")

# ----------------------------------
# 5. Hotel Booking
# A guest can check in only if they have a valid ID.

# If they have ID:
# If age is 18 or above
# Print "Room Booked"
# Else
# Print "Minor Cannot Book Alone"
# Else
# Print "Valid ID Required"

valid_id = int(input("Do you have a valid ID? (1 for Yes, 0 for No): "))

if valid_id == 1:
    age = int(input("Enter your age: "))
    if age >= 18:
        print("Room Booked")
    else:
        print("Minor Cannot Book Alone")
else:
    print("Valid ID Required")



# ----------------------------------
# 6. Phone Unlock
# A phone unlocks only if the password is correct.

# If password is correct:
# If fingerprint matches
# Print "Phone Unlocked"
# Else
# Print "Fingerprint Failed"
# Else
# Print "Wrong Password"

password_correct = input("Enter the password: ")

if password_correct == "admin123":
    fingerprint_match = input("Does the fingerprint match? (yes/no): ")
    if fingerprint_match == "yes":
        print("Phone Unlocked")
    else:
        print("Fingerprint Failed") 
else:
    print("Wrong Password")


# ----------------------------------
# 7. Cricket Team Selection
# A player can attend trials only if age is below 25.
# If eligible:

# If fitness score is above 80
# Print "Selected for Camp"
# Else
# Print "Improve Fitness"
# Else
# Print "Age Limit Exceeded"


age = int(input("Enter your age: "))

if age < 25:
    fitness_score = int(input("Enter your fitness score: "))
    if fitness_score > 80:
        print("Selected for Camp")
    else:
        print("Improve Fitness")
else:
    print("Age Limit Exceeded")

# ----------------------------------
# 8. Flight Boarding
# Passengers can board only if they have a ticket.

# If ticket available:
# If passport verified
# Print "Board Flight"
# Else
# Print "Passport Verification Needed"
# Else
# Print "Ticket Required"

ticket_available = int(input("Do you have a ticket? (1 for Yes, 0 for No): "))

if ticket_available == 1:
    passport_verified = int(input("Has passport been verified? (1 for Yes, 0 for No): "))
    if passport_verified == 1:
        print("Board Flight")
    else:
        print("Passport Verification Needed")
else:
    print("Ticket Required")

# ----------------------------------
# 9. Company Interview
# Candidates can attend interview only if graduation percentage is at least 60.

# If eligible:
# If aptitude marks are 70 or above
# Print "HR Interview"
# Else
# Print "Technical Practice Needed"
# Else
# Print "Not Eligible"

percentage = float(input("Enter your graduation percentage: "))

if percentage >= 60:
    aptitude_marks = float(input("Enter your aptitude marks: "))
    if aptitude_marks >= 70:
        print("HR Interview")
    else:
        print("Technical Practice Needed")
else:
    print("Not Eligible")
    

# ----------------------------------
# 10. Smart Door Lock
# Door opens only if PIN is correct.

# If PIN correct:
# If face recognition succeeds
# Print "Door Opened"
# Else
# Print "Face Recognition Failed"
# Else
# Print "Incorrect PIN"

pin_correct = int(input("Enter the PIN: "))

if pin_correct == 1234:
    face_recognition = input("Does face recognition succeed? (yes/no): ")
    if face_recognition == "yes":
        print("Door Opened")
    else:
        print("Face Recognition Failed")
else:
    print("Incorrect PIN")