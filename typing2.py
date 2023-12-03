
from selenium.webdriver.common.by import By
import keyboard

from selenium.webdriver import Firefox
url = 'https://humanbenchmark.com/tests/typing'
browser = Firefox()
browser.get(url)

words = browser.find_elements(By.CLASS_NAME, "incomplete")
plaintext = []
for i in words:
    if i.text != "":
        plaintext.append(i.text)
    else:
        plaintext.append(" ")
s = ''.join(plaintext)
keyboard.write(s)