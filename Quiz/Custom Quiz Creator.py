import turtle
                                    #A Custom quiz creator!!
screen = turtle.Screen()
screen.bgcolor("White")

creator = turtle.Turtle()
creator.color("blue")           #Preparing Screen
creator.speed(2)

print("Hello, this is the Quiz creator..")
print("Send me the Statement and options and I'll Create a single turtle quiz from it...")
print("Now let's start the creation..")
s=input("Enter the statement==> ")
o1=input("Enter the 1st Option==> ")
o2=input("Enter the 2nd Option==> ")
o3=input("Enter the 3rd Option==> ")        #Editor
o4=input("Enter the 4th Option==> ")
c=input("Tell the correct option==>")
o=input("Confirm changes?(y/n)")
if o == "y":
    creator.setpos(-315, 240)
    creator.write("Hello this is a custom quiz!", font=("Comic Sans MS", 15, "normal"))
    creator.setpos(-315, 220)
    creator.write("The question is...", font=("Comic Sans MS", 15, "normal"))
    creator.setpos(-315, 180)
    creator.write(s, font=("Comic Sans MS", 25, "normal"))
    creator.setpos(-315, 160)
    creator.write(o1, font=("Comic Sans MS", 15, "normal"))
    creator.setpos(-315, 140)
    creator.write(o2, font=("Comic Sans MS", 15, "normal"))         #This will be on screen
    creator.setpos(-315, 120)
    creator.write(o3, font=("Comic Sans MS", 15, "normal"))
    creator.setpos(-315, 100)
    creator.write(o4, font=("Comic Sans MS", 15, "normal"))
    a=input("Enter the correct option==> ")
    if a == c:
        creator.clear()
        creator.setpos(-315, 160)
        creator.write("THAT'S RIGHT!! GREAT!", font=("Comic Sans MS", 25, "normal"))
        creator.hideturtle()
        turtle.done()
    else:                                                            #Checker
        creator.clear()
        creator.setpos(-315, 160)
        creator.write("THAT'S WRONG", font=("Comic Sans MS", 25, "normal"))
        creator.hideturtle()
        turtle.done()
else:
    exit()