# Make sure to also use:
# pip install pynput and pip install pyautogui

import pyautogui
from pynput import keyboard

stop_execution = False

def on_press(key):
    global stop_execution
    if key == keyboard.Key.esc:
        print("Stopped by user.")
        stop_execution = True


listener = keyboard.Listener(on_press=on_press)
listener.start()

while not stop_execution:
    pyautogui.click()


pyautogui.moveTo(x=500, y=500)


listener.stop()
listener.join()
