print("Hi! :)")
print("I am a determiner designed in Python")
print("I can determine if any number is with relation to the other")
print(" including any relations...")
print("Ok, Now")                    #A calculator, but with Logical operations
a= input("Enter your 1st number:- ")
b= input("Enter your 2nd number:- ")
x= input("Now, enter the operation you have to use (only use >,<,==,!=,>=,<= ):")
if x == ">":
    print("determining...")
    print("Ok, is the first number greater than the second number? ===> ",float(a) > float(b))  #>
    print("Thank you for using me")
    exit()
elif x == "<":
    print("determining...")
    print("Ok, is the first number smaller than the second number?===> ",float(a) < float(b))   #<
    print("Thank you for using me")
    exit()
elif x == "==":
    print("determining...")
    print("Ok, is the first number equal to the second number?===> ",float(a) == float(b))  #=
    print("Thank you for using me")
    exit()
elif x == "!=":
    print("determining...")
    print("Ok, is the first number not equal to the second number?===> ",float(a) != float(b))  #≠
    print("Thank you for using me")
    exit()
elif x == ">=":
    print("determining...")
    print("Ok, is the first number greater than or equal to the second number?===> ",float(a) >= float(b))  #≥
    print("Thank you for using me")
    exit()
elif x == "<=":
    print("determining...")
    print("Ok, is the first number smaller than or equal to the second number?===> ",float(a) <= float(b))  #≤
    print("Thank you for using me")
    exit()
elif x == "#":
    print("Nothing here currently...")      #As it says... Nothing
    exit()
else:
    print("!ERROR 101!")
    print("NO SUCH OPERATION")      #Anything else
    exit()