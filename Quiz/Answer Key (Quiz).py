import turtle
                                    #The key to the quizzes
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor("green")
                                    #Preparing Turtle and Screen
key = turtle.Turtle()
key.color("black")
key.speed(2)

print("This is the ultimate Master Answer Key to all my quizzes")
print("Whether it be Science or GK..")

x= input("But first, Enter the X Code==> ")   #My Personal code
if x == "XENON2580":
    print("Ok now you are verified..")
    q= input("Enter the COC==> ")    #COC= Code for quizzes
    if q == "SCI2468":
        print("Great! Generating the answer key...")
        key.penup
        key.goto(-315, 240)
        key.pendown
        key.write("1. c) Proxima Centauri")
        key.penup
        key.goto(-315, 220)
        key.pendown
        key.write("2. b) Sulfuric Acid")
        key.penup
        key.goto(-315, 200)
        key.pendown
        key.write("3. a) 2.13 M")
        key.penup
        key.goto(-315, 180)
        key.pendown
        key.write("4. d) Reykjavik")
        key.penup
        key.goto(-315, 160)
        key.pendown
        key.write("5. b) North Atlantic Treaty Organization")
        key.penup
        key.goto(-315, 140)
        key.pendown
        key.write("6. b) Inca Empire")
        key.penup
        key.goto(-315, 120)
        key.pendown
        key.write("7. c) Budget deficit")
        key.penup
        key.goto(-315, 100)
        key.pendown
        key.write("8. a) Dopamine")
        key.penup
        key.goto(-315, 80)
        key.pendown
        key.write("9. d) Compilation")
        key.penup
        key.goto(-315, 60)
        key.pendown
        key.write("10. b) 119")
        turtle.done()
        exit()
    else:
        exit()
else:
    exit()