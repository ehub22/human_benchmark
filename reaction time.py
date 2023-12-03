import mouse
import pyautogui
from PIL import Image
import keyboard
import time

def check():
    while True:
        if not pyautogui.pixelMatchesColor(500, 500, (206, 38, 54)):
            mouse.click("left")
            break
    return True


keyboard.send("alt+tab")
time.sleep(0.3)
keyboard.send("ctrl+t")
keyboard.write("https://humanbenchmark.com/tests/reactiontime")
keyboard.send("enter")
time.sleep(1)
green = Image.open("green.png")
for i in range(5):
    mouse.move(800,500)
    mouse.click("left")
    time.sleep(0.5)
    check()
    time.sleep(1)