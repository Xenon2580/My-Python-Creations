print("Hey there!")
print("Let's play Tic-tac-toe (2P)")    #Introduction
print("ax","|","ay","|","az")
print("-","+","-","+","-",)
print("bx","|","by","|","bz")
print("-","+","-","+","-",)
print("cx","|","cy","|","cz")
p1=input("Enter 1st player name==> ")   #Names
p2=input("Enter 2nd player name==> ")
ax,ay,az,bx,by,bz,cx,cy,cz=" "," "," "," "," "," "," "," "," ", #Blanks
flag=0
while flag == 0:
    print(ax,"|",ay,"|",az)
    print("-","+","-","+","-",)
    print(bx,"|",by,"|",bz)           #Showing screen
    print("-","+","-","+","-",)
    print(cx,"|",cy,"|",cz)
    print(p1, ", Your turn")
    in1=input("Please enter the cell where you want to put circle...")  
    if in1 == "ax":
        ax = "O"
    elif in1 == "bx":
        bx = "O"
    elif in1 == "cx":
        cx = "O"
    elif in1 == "ay":
        ay = "O"
    elif in1 == "by":
        by = "O"                         #p1 time
    elif in1 == "cy":
        cy = "O"
    elif in1 == "az":
        az = "O"
    elif in1 == "bz":
        bz = "O"
    elif in1 == "cz":
        cz = "O"
    else:
        print("!!ERROR!!")
    print(ax,"|",ay,"|",az)
    print("-","+","-","+","-",)
    print(bx,"|",by,"|",bz)                     #Showing screen
    print("-","+","-","+","-",)
    print(cx,"|",cy,"|",cz)
    if ax == ay == az:
        if ax == "O":
            print(p1, " wins the game!!!")
            flag = 1
            break
        else:
            if ax == "X":
                print(p2, " wins the game!!!")
                flag = 1
                break
    elif bx == by == bz:
        if bx == "O":
            print(p1, " wins the game!!!")
            flag = 1
            break
        else:
            if bx == "X":
                print(p2, " wins the game!!!")
                flag = 1
                break
    elif cx == cy == cz:
        if cx == "O":
            print(p1, " wins the game!!!")
            flag = 1
            break
        else:
            if cx == "X":
                print(p2, " wins the game!!!")
                flag = 1
                break
    elif ax == bx == cx:
        if ax == "O":
            print(p1, " wins the game!!!")
            flag = 1
            break
        else:
            if ax == "X":
                print(p2, " wins the game!!!")
                flag = 1
                break
    elif ay == by == cy:
        if ay == "O":
            print(p1, " wins the game!!!")
            flag = 1
            break
        else:
            if ay == "X":
                print(p2, " wins the game!!!")
                flag = 1
                break
    elif az == bz == cz:
        if az == "O":
            print(p1, " wins the game!!!")
            flag = 1
            break
        else:
            if az == "X":
                print(p2, " wins the game!!!")
                flag = 1
                break
    elif ax == by == cz:
        if ax == "O":
            print(p1, " wins the game!!!")
            flag = 1
            break
        else:
            if ax == "X":
                print(p2, " wins the game!!!")
                flag = 1
                break
    elif az == by == cx:
        if az == "O":
            print(p1, " wins the game!!!")
            flag = 1
            break
        else:
            if az == "X":
                print(p2, " wins the game!!!")
                flag = 1
                break
    print(p2, ", Your turn")
    in2=input("Please enter the cell where you want to put cross...")
    if in2 == "ax":
        ax = "X"
    elif in2 == "bx":
        bx = "X"
    elif in2 == "cx":
        cx = "X"
    elif in2 == "ay":
        ay = "X"
    elif in2 == "by":
        by = "X"                         #p2 time
    elif in2 == "cy":
        cy = "X"
    elif in2 == "az":
        az = "X"
    elif in2 == "bz":
        bz = "X"
    elif in2 == "cz":
        cz = "X"
    else:
        print("!!ERROR!!")
    if ax == ay == az:
        if ax == "O":
            print(p1, " wins the game!!!")
            flag = 1
            break
        else:
            if ax == "X":
                print(p2, " wins the game!!!")
                flag = 1
                break
    elif bx == by == bz:
        if bx == "O":
            print(p1, " wins the game!!!")
            flag = 1
            break
        else:
            if bx == "X":
                print(p2, " wins the game!!!")
                flag = 1
                break
    elif cx == cy == cz:
        if cx == "O":
            print(p1, " wins the game!!!")
            flag = 1
            break
        else:
            if cx == "X":
                print(p2, " wins the game!!!")
                flag = 1
                break
    elif ax == bx == cx:
        if ax == "O":
            print(p1, " wins the game!!!")
            flag = 1
            break
        else:
            if ax == "X":
                print(p2, " wins the game!!!")
                flag = 1
                break
    elif ay == by == cy:
        if ay == "O":
            print(p1, " wins the game!!!")
            flag = 1
            break
        else:
            if ay == "X":
                print(p2, " wins the game!!!")
                flag = 1
                break
    elif az == bz == cz:
        if az == "O":
            print(p1, " wins the game!!!")
            flag = 1
            break
        else:
            if az == "X":
                print(p2, " wins the game!!!")
                flag = 1
                break
    elif ax == by == cz:
        if ax == "O":
            print(p1, " wins the game!!!")
            flag = 1
            break
        else:
            if ax == "X":
                print(p2, " wins the game!!!")
                flag = 1
                break
    elif az == by == cx:
        if az == "O":
            print(p1, " wins the game!!!")
            flag = 1
            break
        else:
            if az == "X":
                print(p2, " wins the game!!!")
                flag = 1
                break
