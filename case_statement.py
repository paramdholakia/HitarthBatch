""" 

match variable_name:
    case value1:
        # Code block for value1
    case value2:
        # Code block for value2
    case value3:
        # Code block for value3
    case _:
        # Default code block for any other value

"""

user_input = input("Enter a option (Play/Options/Quit): ")

match user_input:
    case "Play":
        print("Starting the game...")
        # Add code to start the game here
    case "Options":
        print("Opening options menu...")
        # Add code to display options menu here
    case "Quit":
        print("Exiting the game. Goodbye!")
        # Add code to exit the game here
    case _:
        print("Invalid option. Please try again.")
        # Add code to handle invalid input here