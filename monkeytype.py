
from selenium.webdriver.common.by import By
import keyboard
import time


from selenium.webdriver import Firefox
url = 'https://monkeytype.com/'
browser = Firefox()
browser.get(url)
browser.fullscreen_window()

try:
    browser.find_element(By.XPATH, "/html/body/div[8]/div/div[2]/div[2]/div[2]/button[1]").click()
except:
    pass
time.sleep(1)
browser.find_element(By.XPATH, "/html/body/div[9]/div[2]/main/div/div[1]/div/div[5]/div[4]").click()
time.sleep(2)
while True:
    elements = browser.find_element(By.XPATH, "//*[@class='word active']")
    keyboard.write(elements.text+" ")
    time.sleep(0.015)
