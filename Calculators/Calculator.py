print("Hi! :)")                 #My most accurate Calculator
print("I am a calculator designed in Python")       #Remember the result would be in Float
print("I can solve any of your arithmetic problem")
print("Whether it's Addition, Substraction, Multiplication, Division, Powers and Remainders")
print("Ok, Now")
a= input("Enter your 1st number:- ")    #Selecting Numbers
b= input("Enter your 2nd number:- ")
x= input("Now, enter the operation you have to use (only use +,-,*,/,**,%):")   #Selecting Operation
if x == "+":
    print("calculating...")
    print("Ok, so the Sum of these two numbers would be===> ",float(a) + float(b))  # ADD
    print("Thank you for using me")
    exit()
elif x == "-":
    print("calculating...")
    print("Ok, so the Difference of these two numbers would be===> ",float(a) - float(b))   #SUB
    print("Thank you for using me")
    exit()
elif x == "*":
    print("calculating...")
    print("Ok, so the Product of these two numbers would be===> ",float(a) * float(b))  #MULT
    print("Thank you for using me")
    exit()
elif x == "/":
    print("calculating...")
    print("Ok, so the Quotient of these two numbers would be===> ",float(a) / float(b)) #DIV
    print("Thank you for using me")
    exit()
elif x == "**":
    print("calculating...")
    print("Ok, so the Power of the given number would be===> ",float(a) ** float(b))    #POW
    print("Thank you for using me")
    exit()
elif x == "%":
    print("calculating...")
    print("Ok, so the Remainder of these two numbers would be===> ",float(a) % float(b))    #REM
    print("Thank you for using me")
    exit()
elif x == "#":
    print("Nothing here currently...")  #As it says... Nothing
    exit()
else:
    print("!ERROR 101!")
    print("NO SUCH OPERATION") #Anything else
    exit()