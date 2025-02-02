print("Hi! :)")
print("I am a calculator designed in Python")       #A Calculator, but with infinite no. of operations
print("I can solve any of your arithmetic problem")
print("Whether it's Addition, Substraction, Multiplication or Division")
print("And can execute commands endlessly")
print("Ok, Now")
first_no= int(input("Enter your 1st number:- "))
flag=0
while flag == 0:
    next_no= int(input("Enter your next number:- "))
    operator= input("Enter the variable(+,-,*,/):- ")
    if operator == "+":
        final_no=int(first_no + next_no)    #+
    elif operator == "-":
        final_no=int(first_no - next_no)    #-
    elif operator == "*":
        final_no=int(first_no * next_no)    #*
    elif operator == "/":
        final_no=int(first_no / next_no)    #/
    else:
        print("Please enter a valid operator!!")
        exit()
    go_on= input ("Do you want to continue??")
    if go_on == "y":
        print("OK, let's go on")
        flag=0                          #Checks the flag
    elif go_on == "n":
        print("Got it!")
        flag=1
    else:
        print("Please enter either y or n") #Anything Else
        exit()
print("Calculating final answer...")
print("The final answer would be= ", final_no ) #Output
