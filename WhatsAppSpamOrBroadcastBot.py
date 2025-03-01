# !!!Since we can't create a broadcast group in whatsapp on PC/Laptops, we can use this code to send a message to muliple contacts!!!

# If you believe there is a problem during execution, make sure you stop the program immediately.
# Make sure that before running or executing the software, close all other applications.
# Make sure that after running or executing the software, you don't move or click the mouse or touch the keyboard.
import datetime
import time
import pyautogui
from colorama import init, Fore, Style


# Open WhatsApp installed on PC
def open_whatsapp():
    pyautogui.hotkey("win")
    time.sleep(1)
    pyautogui.write("WhatsApp")
    time.sleep(1)
    pyautogui.press("enter")
    # Adjust the sleep time based on the system's speed
    time.sleep(5)


def multi_profile(number):
    steps = 1 if number == 1 else 2 * number
    for i in range(steps):
        pyautogui.press("tab")
        time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)


def open_whatsapp_web():
    time.sleep(2)
    # Open WhatsApp installed on PC
    pyautogui.hotkey("win")
    time.sleep(1)
    # Change the browser in which you have whatsapp logged in like brave,edge,chrome,firefox etc
    # !!!This option only works when the user is already logged in using the browser!!!
    pyautogui.write("Brave")
    time.sleep(1)
    pyautogui.press("enter")
    # Adjust the sleep time based on the system's speed
    time.sleep(5)

    # If the browser has multiple profiles, delete the '#' character(uncomment the line) & change the value '1' to the desired profile number, counting one by one from left to right.
    # multi_profile(1)

    pyautogui.write("web.whatsapp.com")
    time.sleep(1)
    pyautogui.press("enter")
    # Adjust the sleep time based on the whatsapp loading time
    time.sleep(25)


def send_messages_web(phone_numbers, message, repeat):
    for number in phone_numbers:
        time.sleep(1)
        pyautogui.hotkey("ctrl", "alt", "/")
        time.sleep(1)
        pyautogui.write("temp")
        time.sleep(1)
        pyautogui.hotkey("ctrl", "a")
        time.sleep(2)
        pyautogui.press("delete")
        time.sleep(3)
        pyautogui.write(number)
        time.sleep(3)
        pyautogui.press("down")
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(1)

        for i in range(repeat):
            # (In Terminal)Display the time at which the message is sent
            print("Message sent at:", datetime.datetime.now())
            pyautogui.typewrite(f"{message}", interval=0.05)
            pyautogui.press("enter")
            time.sleep(2)
            pyautogui.keyDown("shift")
            for i in range(3):
                pyautogui.press("tab")
            pyautogui.keyUp("shift")
            time.sleep(1)
            pyautogui.press("right")
            time.sleep(1)
            pyautogui.press("enter")
            time.sleep(1)
            pyautogui.press("up")
            time.sleep(1)
            pyautogui.press("enter")
            time.sleep(1)
            [pyautogui.press("tab") for i in range(2)]
            time.sleep(1)
            pyautogui.press("enter")
            time.sleep(1)
            [pyautogui.press("tab") for i in range(2)]
            time.sleep(1)
            pyautogui.press("enter")
            time.sleep(1)
            pyautogui.keyDown("shift")
            for i in range(2):
                pyautogui.press("tab")
            pyautogui.keyUp("shift")
            time.sleep(1)

        # Close chat and prepare for the next contact
        pyautogui.press("escape")
        time.sleep(2)
        pyautogui.hotkey("ctrl", "alt", "/")
        time.sleep(2)
        pyautogui.hotkey("ctrl", "a")
        time.sleep(2)
        pyautogui.press("delete")
        time.sleep(2)


# The value '2' in the repeat variable can be changed to any number which defines how many times you need to send that message to that phone number/numbers. In this case, the message is sent 2 times.
def send_messages(phone_numbers, message, repeat):
    for number in phone_numbers:
        pyautogui.write(number)
        time.sleep(3)
        pyautogui.press("down")
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(1)

        for i in range(repeat):
            # (In Terminal)Display the time at which the message is sent
            print("Message sent at:", datetime.datetime.now())
            pyautogui.typewrite(f"{message}", interval=0.05)
            time.sleep(2)
            pyautogui.press("enter")
            time.sleep(2)
            for i in range(10):
                pyautogui.press("tab")
                time.sleep(1)
            pyautogui.press("delete")
            time.sleep(1)
            pyautogui.press("down")
            time.sleep(1)
            pyautogui.press("up")
            time.sleep(1)
            pyautogui.press("down")
            time.sleep(1)
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.press("enter")
            time.sleep(1)

        # Close chat and prepare for the next contact
        pyautogui.hotkey("ctrl", "w")
        time.sleep(2)
        pyautogui.hotkey("ctrl", "f")
        time.sleep(2)
        pyautogui.hotkey("ctrl", "a")
        time.sleep(2)
        pyautogui.press("delete")
        time.sleep(2)


if __name__ == "__main__":
    init()
    print(
        Fore.RED + "!!!Welcome to Whatsapp Spam/Broadcast Bot!!!\n"
        "!!!If you believe there is a problem during execution, make sure you stop the program immediately.!!!\n"
        "!!!Make sure that before running or executing the software, close all other applications.!!!\n"
        "!!!Make sure that after running or executing the program/code, you don't move/click the mouse/touch the keyboard.!!!"
        + Style.RESET_ALL
    )

    num = int(input("Enter the no.of phone numbers to spam:"))
    phone_numbers = [input(f"Enter valid phone number {i+1}:") for i in range(num)]
    message = input("Enter the text to be sent/spammed:")
    repeat = int(input("Enter the no.of times the text to be sent/spammed:"))
    print("1)Whatsapp app in PC/Laptop")
    print("2)Whatsapp web in any bowser")
    choice = int(input("Enter your choice:"))
    print("Now donot disturb the PC/Laptop & wait until the program ends")
    time.sleep(2)
    if choice == 1:
        open_whatsapp()
        time.sleep(2)
        send_messages(phone_numbers, message, repeat)
    elif choice == 2:
        open_whatsapp_web()
        time.sleep(2)
        send_messages_web(phone_numbers, message, repeat)
