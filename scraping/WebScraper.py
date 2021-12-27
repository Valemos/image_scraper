import os
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import urllib.request

presence = EC.presence_of_element_located

#%%
with open("secret.yaml") as fin:
    config = yaml.load(fin, yaml.Loader)

profile_username = config["username"]
profile_password = config["password"]

#%%
options = Options()
options.binary = "/home/anton/tools/firefox/firefox"

browser = webdriver.Firefox(options=options)

#%%
browser.get('https://www.instagram.com/')

#%%
wait = WebDriverWait(browser, 10)
wait_ignore = WebDriverWait(browser, 10, ignored_exceptions=[NoSuchElementException, TimeoutException])

browser.implicitly_wait(20)

login = wait.until(presence((By.XPATH, "//input[@name='username']")))
password = wait.until(presence((By.XPATH, "//input[@name='password']")))
login.send_keys(profile_username)
password.send_keys(profile_password)
submit = wait.until(presence((By.XPATH, "//button[@type='submit']")))
submit.click()

#%%
not_now_save_login = wait_ignore.until(presence((By.XPATH, "//button[@class='sqdOP yWX7d    y3zKF     ']")))
not_now_save_login.click()

not_now_notifications = wait_ignore.until(presence((By.XPATH, "//button[@class='aOOlW   HoLwm ']")))
not_now_notifications.click()

#%%

target_profile = "cristiano"
browser.get(f"https://www.instagram.com/{target_profile}")

#%%
profile_icon = browser.find_element(By.XPATH, "//span[@class='_2dbep qNELH']")
profile_icon.click()

#%%

items = browser.find_elements(By.XPATH, "//div[@class='eLAPa']")
print(items)
items[0].click()

#%%
image_element = wait.until(presence((By.XPATH, "//img[@class='FFVAD']")))
print(image_element)
image_source = image_element.get_attribute("src")
urllib.request.urlretrieve(image_source, "result.jpg")

#%%
browser.quit()
