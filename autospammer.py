# AutoSpammer v: 1.0
# Made by: BugzumDev

# importing libs
import keyboard
import time
import os

# Fast screen clear command
def cls():
    os.system("cls")

# Menu
cls()
print()
print("Welcome to AutoSpammer v: 1.0")
print()
print("Made by: BugzumDev")
print()
print("I AM NOT RESPONSIBLE FOR ANY ACCOUNT BAN USING THIS TOOL")
print()
input("[enter] I agree, continue")
cls()
msg = input('Message: ')
msgnum = input('Message number: ')

# Mode setter
while True:
    print("Select mode: ")
    print("[1] Normal mode")
    print("[2] CS:GO mode")
    print("[3] Messenger Automatic mode")
    print("[4] Test mode")
    mode = input()
    if mode in ["1", "2", "3", "4"]:
        break

if mode == "4":
    testnum = input("Test number: ")

input("Variables set, press enter to continue...")
cls()

# Countdown
cls()
print("STARTING 10")
time.sleep(1)
cls()
print("STARTING 9")
time.sleep(1)
cls()
print("STARTING 8")
time.sleep(1)
cls()
print("STARTING 7")
time.sleep(1)
cls()
print("STARTING 6")
time.sleep(1)
cls()
print("STARTING 5")
time.sleep(1)
cls()
print("STARTING 4")
time.sleep(1)
cls()
print("STARTING 3")
time.sleep(1)
cls()
print("STARTING 2")
time.sleep(1)
cls()
print("STARTING 1")
time.sleep(1)
cls()
print("STARTING...")
time.sleep(1)

# Actual spamming functionality
if mode == "1":
    for i in range(int(msgnum)):
        keyboard.write(msg)
        keyboard.press("enter")

elif mode == "2":
    for i in range(int(msgnum)):
        keyboard.write("z")
        keyboard.write(msg)
        keyboard.press("enter")

elif mode == "3":
        for i in range(int(msgnum)):
            keyboard.write("z")
            keyboard.write(msg)
            keyboard.press("enter")
elif mode == "4":
    print("TXT")
    keyboard.write("AutoSpammer Test Mode")
    keyboard.press("enter")
    keyboard.write("Test number: " + testnum)
    keyboard.press("enter")
    keyboard.write("AutoSpammer is made by: BugzumDev")
    keyboard.press("enter")
    keyboard.write("This project is open source and it's uploaded to 'https://github.com/BugzumDev/AutoSpammer'")
    keyboard.press("enter")
    keyboard.write("[PHZ:PREP]: Preparing to test")
    keyboard.press("enter")
    print("PREP")
    time.sleep(2)
    keyboard.write("[PHZ:SEND]: Sending message(s)")
    keyboard.press("enter")
    for i in range(int(msgnum)):
        keyboard.write(msg)
        keyboard.press("enter")
        print("Message " + str(i + 1) + " was sent")
        keyboard.write("[REP:MSG]: Message " + str(i + 1) + " was successfully sent.")
        keyboard.press("enter")
    keyboard.write("[PHZ:END]: Message spamming finished.")
    print("FIN")
    keyboard.press("enter")
    keyboard.write("REQ/SENT: " + msgnum + "/" + str(i + 1))
    print("REQ/SENT: " + msgnum + "/" + str(i + 1))
    keyboard.press("enter")
    keyboard.write("Spamming ended...")
    keyboard.press("enter")
    input()
    exit()

# Finish message
cls()
print("Spamming finished!")
print()
input("Press enter to quit")
exit()