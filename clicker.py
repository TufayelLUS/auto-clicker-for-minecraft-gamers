import pyautogui
from time import sleep
from concurrent.futures import ThreadPoolExecutor
import keyboard


def click():
    pyautogui.leftClick()


def trigger():
    with ThreadPoolExecutor(max_workers=100) as executor:
        for i in range(3000):
            executor.submit(click)
            # sleep(0.1)
            print("clicked")


def on_key_press():
    print("You pressed the 'a' key!")
    trigger()


# Monitor the 'a' key and call on_key_press when it's pressed
keyboard.on_press_key('a', lambda _: on_key_press())

# Keep the program running to monitor the keyboard
print("Press 'a' to trigger the function. Press 'esc' to exit.")
keyboard.wait('esc')  # The program will stop when 'esc' is pressed
