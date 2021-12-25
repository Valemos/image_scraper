import os
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

presence = EC.presence_of_element_located

#%%
with open("secret.yaml") as fin:
    config = yaml.load(fin, yaml.Loader)

profile_username = config["username"]
profile_password = config["password"]

#%%
browser = webdriver.Firefox()

#%%
browser.get("https://www.instagram.com/")

#%%
wait = WebDriverWait(browser, 10)
wait_ignore = WebDriverWait(browser, 10, ignored_exceptions=[NoSuchElementException, TimeoutException])

browser.implicitly_wait(10)

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

browser.get(f"https://www.instagram.com/{profile_username}")

#%%
profile_icon = browser.find_element(By.XPATH, "//span[@class='_2dbep qNELH']")
profile_icon.click()

#%%

items = browser.find_elements(By.XPATH, "//div[@class='v1Nh3 kIKUG  _bz0w']")
print(items)
items[0].click()

#%%
browser.quit()
