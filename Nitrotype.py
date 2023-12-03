from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
import keyboard
import time

from selenium.webdriver import Firefox
url = 'https://www.nitrotype.com/'
browser = Firefox()
browser.get(url)
time.sleep(1)

time.sleep(30)


while True:
    elements = WebDriverWait(browser, 25).until(visibility_of_element_located((By.XPATH, "//*[@class='dash-letter is-waiting']")))
    keyboard.write(elements.text)
    time.sleep(0.015)
