import random

playermar = botmar = 0
name = input("Enter your name==> ")                                 #initial
total = int(input("Enter the total number of marbles in the game==> "))
playermar = botmar = total // 2

print("Let's start")

while playermar > 0 and botmar > 0:
    first = random.randint(0, 1)
    if first == 1:
        print("Let's start with you...")    #Start with User
        while playermar > 0 and botmar > 0:
            while True:
                player = input(f"Enter the number of marbles you want to place (1 to {playermar}) ==> ")
                if player.isdigit() and 1 <= int(player) <= playermar:
                    player = int(player)
                    break
                print(f"Invalid input. Please enter a number between 1 and {playermar}.")
            bot = random.randint(1, botmar)
            if bot % 2 == player % 2:                           #ODD/EVEN
                print("Opponent guessed correctly")
                playermar = playermar - player
                botmar = botmar + player                        #Change marbles
            else:
                print("Opponent guessed incorrectly")
    else:
        print("Let's start with your opponent")     #Now bot time
        bot = random.randint(1, botmar)
        print("Opponent has placed the marbles...")
        while True:
            player = input(f"Enter the number of marbles you want to place (1 to {playermar}) ==> ")
            if player.isdigit() and 1 <= int(player) <= playermar:
                player = int(player)
                break
            print(f"Invalid input. Please enter a number between 1 and {playermar}.")
        if player % 2 == bot % 2:                           #ODD/EVEN
            print("You guessed correctly")
            botmar = botmar - bot
            playermar = playermar + bot                        #Change marbles
        else:
            print("You are incorrect")
if playermar > 0:
    print("You Won!!")
else:
    print("You Lost!!")
