print("I am a temperature calculator designed in Python")
print("I can calculate the temperature between Celsius, Fahrenheit and Kelvin ")    #A calculator, but with temprature
x= input("Enter the temperature:- ")
a= input("Enter the initial unit (c/f/k):- ")       #Input
b= input("Enter the final unit (c/f/k) :- ")
if a == "c":
    print("Intitial unit 'CELSIUS selected'")       #Selecting initial
    if b == "c":
        print("!!SAME UNIT!! #CELSIUS#")
    elif b == "f":
        print("Conversion= CELSIUS--->FAHRENHEIT")  #Selecting Final
        print( float(x) * 1.8000 + 32.00)           #Conversion
    elif b == "k":
        print("Conversion= CELSIUS--->KELVIN")
        print(float(x) + 273.15)
    else:
        print("ERROR")                              #Something Wrong
        exit()
elif a == "f":
    print("Intitial unit 'FAHRENHEIT selected'")
    if b == "f":
        print("!!SAME UNIT!! #FAHRENHEIT#")
    elif b == "c":
        print("Conversion= FAHRENHEIT--->CELSIUS")
        print( (float(x) - 32)/1.8000)
    elif b == "k":
        print("Conversion= FAHRENHEIT--->KELVIN")
        print( ( (float(x)- 32)/1.8000 ) + 273.15)
    else:
        print("ERROR")
        exit()
elif a == "k":
    print("Intitial unit 'KELVIN selected'")
    if b == "k":
        print("!!SAME UNIT!! #KELVIN#")
    elif b == "c":
        print("Conversion= KELVIN--->CELSIUS")
        print(float(x) - 273.15)
    elif b == "f":
        print("Conversion= KELVIN--->FAHRENHEIT")
        print(((float(x) - 273.15) * 1.8) + 32)
    else:
        print("ERROR")
        exit()
else:
    print("ERROR")
    exit()