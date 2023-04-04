import random
from faker import Faker
from selenium import webdriver
import time

fake = Faker()
from selenium.webdriver.common.by import By


with open('emails.txt', 'r') as f:
    email_list = f.read().splitlines()

path_to_chromedriver = 'chromedriver.exe'
browser = webdriver.Chrome(executable_path=path_to_chromedriver)
browser.implicitly_wait(10)

browser.get('https://www.epicgames.com/id/register/date-of-birth')


start_time = time.time()
dates_select = browser.find_elements(By.CLASS_NAME, 'MuiOutlinedInput-input')
dates_select[0].click()
# time.sleep(0.25)
second = browser.find_elements(By.CLASS_NAME, 'MuiListItem-button')
second[random.randint(0, 13)].click()

dates_select[1].click()
# time.sleep(0.25)
ge = browser.find_elements(By.CLASS_NAME, 'MuiListItem-button')
ge[random.randint(0, 2)].click()
dates_select[2].click()
# time.sleep(0.25)
dates_select[2].send_keys("2001")
# time.sleep(0.25)
browser.find_element(By.ID, "continue").click()
# time.sleep(0.5)

browser.find_element(By.ID, 'name').send_keys(fake.first_name())
browser.find_element(By.ID, 'lastName').send_keys(fake.last_name())
browser.find_element(By.ID, 'displayName').send_keys(fake.unique.user_name() + str(random.randint(100, 10000)))
browser.find_element(By.ID, 'email').send_keys(email_list[0])
browser.find_element(By.ID, 'password').send_keys(fake.password())
browser.find_element(By.ID, 'tos').click()

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Registration time per 1 account: {elapsed_time:.2f} секунд")
# browser.find_element(By.ID, 'btn-submit').click()

browser.quit()
