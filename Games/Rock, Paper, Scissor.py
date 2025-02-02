import random

flag=0
print("Let's play Rock, Paper and Scissors with Bot")       #Initials

while flag == 0:
    user = input("Enter Rock, Paper, or Scissors: ").lower()
    bot = random.choice(['rock', 'paper', 'scissors'])                            #Player's Inputs

    print(f"Computer chose: {bot}")

    if user == bot:
        print("It's a tie!")
    elif (user == "r" and bot == 's') or (user == "s" and bot == 'p') or (user == "p" and bot == 'r'):
        print("You won!")
    else:                                          #Decision
        print("You lost!")

    loop=input("Wanna play again? (y/n)")
    if loop == "Yes" or "y":
        flag=0
    else:                                             #loop
        flag=1