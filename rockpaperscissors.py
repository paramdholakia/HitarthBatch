while True:
    print("Do you want to start a new game? if yes type Y else N")
    userChoice = input("Enter your Choice : ")

    if userChoice == "N":
        print("Exiting the game")
        break

    print("Welcome to Rock Paper Scissors!")
    print("1 = Rock")
    print("2 = Paper")
    print("3 = Scissors")

    player1 = int(input("Player 1 Choose your action : "))
    player2 = int(input("Player 2 Choose your action : "))

    if player1 == 1:
        if player2 == 2:
            print("Player 2 wins")
        elif player2 == 3:
            print("Player 1 Wins") 
        else:
            print("It's a TIE!")
    elif player1 == 2:
        if player2 == 3:
            print("Player 2 wins")
        elif player2 == 1:
            print("Player 1 Wins") 
        else:
            print("It's a TIE!")
    else:
        if player2 == 1:
            print("Player 2 wins")
        elif player2 == 2:
            print("Player 1 Wins") 
        else:
            print("It's a TIE!")