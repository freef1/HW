from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('./chromedriver.exe')
driver.get('http://itcareer.pythonanywhere.com')

# web_form = driver.find_element(By.CLASS_NAME, 'form-group')
# print(web_form.get_attribute('innerHTML'))


name_field = driver.find_element(By.ID, 'name')
name_field.send_keys('Evgenii')
time.sleep(1)

surname_field = driver.find_element(By.ID, 'surname')
surname_field.send_keys('Klichevskii')
time.sleep(1)

email_field = driver.find_element(By.ID, 'email')
email_field.send_keys('lebronvince07@gmail.com')
time.sleep(1)

password_field = driver.find_element(By.ID, 'password')
password_field.send_keys('12345qwerty')
time.sleep(1)

submit_button = driver.find_element(By.TAG_NAME, 'button')
submit_button.click()

success_message = driver.find_element(By.TAG_NAME, 'strong')
print(success_message.text)

message_path = '/html/body/div[2]/div/div/div'
success_message_2 = driver.find_element(By.XPATH, message_path)

if 'Success' in success_message_2.text:
    print('Test_success_message - PASSED')
else:
    print('Test_success_message - FAILED')


time.sleep(3)


driver.close()