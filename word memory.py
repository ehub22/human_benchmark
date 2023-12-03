from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
import time


url = 'https://humanbenchmark.com/tests/verbal-memory'
browser = Firefox()
browser.get(url)
l = browser.find_element(By.XPATH, "/html/body/div/div/div[4]/div[1]/div/div/div/div[4]/button")
browser.execute_script("arguments[0].click();", l)
print("Started")
word_list=[]
while True:
    word = browser.find_element(By.XPATH, "/html/body/div/div/div[4]/div[1]/div/div/div/div[2]/div")
    word = word.text
    if word not in word_list:
        word_list.append(word)
        new = browser.find_element(By.XPATH, "/html/body/div/div/div[4]/div[1]/div/div/div/div[3]/button[2]")
        browser.execute_script("arguments[0].click();", new)
    elif word in word_list:
        old = browser.find_element(By.XPATH, "/html/body/div/div/div[4]/div[1]/div/div/div/div[3]/button[1]")
        browser.execute_script("arguments[0].click();", old)