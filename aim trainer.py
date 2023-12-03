import pyautogui
import keyboard
import time
from PIL import Image
import mouse
target2 = Image.open("target.png")
keyboard.send("alt+tab")
time.sleep(0.3)
keyboard.send("ctrl+t")
time.sleep(0.1)
keyboard.write("https://cps-check.com/jitter-click-test-60")
keyboard.send("enter")
time.sleep(1)
while True:
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(target2)
    mouse.move(target[0]+50, target[1]+50)
    mouse.click("left")