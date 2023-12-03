from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox
import time
from lxml import etree

url = 'https://humanbenchmark.com/tests/sequence'
browser = Firefox()
browser.get(url)

time.sleep(1)

browser.find_element(By.XPATH, "/html/body/div/div/div[4]/div[1]/div/div/div/div[2]/button").click()

level = 1
while True:
    for i in range(level):
        time.sleep(0.2)
        element = browser.find_element(By.CLASS_NAME, "square active")
        print(element)