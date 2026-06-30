from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
parent_window = driver.current_window_handle
driver.implicitly_wait(10)
driver.find_element(By.CSS_SELECTOR, "a[href='https://rahulshettyacademy.com/documents-request']").click()

child_window = driver.window_handles
driver.switch_to.window(child_window[1])
email_para = driver.find_element(By.CSS_SELECTOR, ".red").text
print(email_para)

words = email_para.split()
email = ""
for word in words:
    if "@" in word:
        email = word
        break
print(email)
print(repr(email))


driver.switch_to.window(parent_window)
print(driver.title)
driver.find_element(By.ID, "username").send_keys(email)
driver.find_element(By.ID, "password").send_keys("learning")
driver.find_element(By.ID, "signInBtn").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME , "alert-danger")))
alert_text = driver.find_element(By.CLASS_NAME , "alert-danger").text
print(alert_text)

assert "Incorrect username/password." in alert_text
