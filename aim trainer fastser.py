from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox
import time

url = 'https://humanbenchmark.com/tests/aim'
browser = Firefox()
browser.get(url)
time.sleep(4)
while True:
    browser.find_element(By.XPATH, "//a[@id=root]/div/div[4]/div[1]/div/div[1]/div[2]/div/div/div[6]").click()