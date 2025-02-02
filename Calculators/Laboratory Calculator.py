print("Hello There! :)")
print("I am the Ultimate Chemistry Calculator designed in Python")
print("I can solve most of Chemical Calculations")  #A calculator but for laboratories
print("Be it Molarity, Molality, finding volume")
print("Ok, Now")
print("Which Calculator would you like to use??")
print("1. Molarity, 2. Molality, 3. Mass %, 4. Mole fraction, 5. Finding Mass, 6. Finding Sign. figure")
x = input("Enter the Resp. number here==> ")    #Choose function

if x == "1":
    print("Ok, You've chosen MOLARITY")
    a = float(input("Enter the No. of Moles of Solute=> "))
    b = float(input("Enter the Volume of solution (L)=> "))
    print("processing...")                                      #M
    print("So the molarity of the solution would be", a / b)
    exit()
elif x == "2":
    print("Ok, You've chosen MOLALITY")
    a = float(input("Enter the No. of Moles of Solute=> "))
    b = float(input("Enter the Mass of Solvent (Kg)=> "))
    print("processing...")                                      #m
    print("So the molality of the solution would be", a / b, "m")
    exit()
elif x == "3":
    print("Ok, You've chosen MASS %")
    a = float(input("Enter the Mass of Solute=> "))
    b = float(input("Enter the Mass of Solution=> "))
    print("processing...")                                      #m%
    print("So the mass percentage of the solution would be", (a / b) * 100, "%" )
    exit()
elif x == "4":
    print("Ok, You've chosen MOLE FRACTION")
    a = float(input("Enter the No. of Moles of the Component=> "))
    b = float(input("Enter the No. of Moles of the Solution (without the comp.)=> "))
    print("processing...")                                       #M/m
    print("So the mole fraction of the component would be", a / (a + b))
    exit()
elif x == "5":
    print("Ok, You've chosen FINDING MASS OF A REACTANT/PRODUCT (up to 2 each)")
    y = input("Enter what to find (0=reactant, 1=product)==>")
    if y == "0":                                                   #Finding mass for 4th Compuond in a 2-2 Reaction
        a2 = float(input("Enter mass of the other Reactant=> "))
        b1 = float(input("Enter mass of First Product=> "))
        b2 = float(input("Enter mass of Second Product=> "))
        print("processing...")
        print("So the mass of the reactant would be", (b1 + b2) - a2)
        exit()
    elif y == "1":
        a1 = float(input("Enter mass of the First Reactant=> "))
        a2 = float(input("Enter mass of Second Reactant=> "))
        b2 = float(input("Enter mass of the other product=> "))
        print("processing...")
        print("So the mass of the product would be", (a1 + a2) - b2)
        exit()
    else:
        print("Please enter either 1 or 0")
        exit()
elif x == "6":
    print("Ok, You've chosen FINDING SIGNIFICANT FIGURES")      #Finding Sig. Fig.
    no = input("Enter the Number: ")
    c = 0

    for i in no:
        if i != "0" and i != ".":               #Rule 1
            c += 1

    for i in range(1, len(no) - 1):               #Rule 2
        if no[i] == "0" and no[i - 1].isdigit() and no[i + 1].isdigit():
            c += 1

    lz = 0
    for i in no:
        if i == "0":               #Rule 3
            lz += 1
        elif i.isdigit():
            break

    td = 0
    if "." in no:               #Rule 4
        for i in reversed(no):
            if i == "0":
                td += 1
            elif i == ".":
                break
            else:
                break
        c += td

    tw = 0
    if "." not in no:               #Rule 5
        for i in reversed(no):
            if i == "0":
                tw += 1
            else:
                break

    print(f"The total no. of Significant digits are: {c}")
    exit()
else:
    print("!!ERROR 101!!")
    print("NO SUCH OPERATION")          #Anything else
    exit()
