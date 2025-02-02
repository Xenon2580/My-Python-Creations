import time
import keyboard

flag = 0                    #initials
seconds = 0

input("Press ENTER to Start and hold SPACE to Stop")
while flag == 0:
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60           #S-M-H
    secs = seconds % 60
    print(f"\r{hours:02}:{minutes:02}:{secs:02}", end="")
    time.sleep(1)               #Space
    seconds += 1
    if keyboard.is_pressed("space"):
        break