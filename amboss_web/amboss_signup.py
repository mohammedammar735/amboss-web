
import random
import string
import time
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Generate fake user data
fake = Faker()
first_name = fake.first_name()
last_name = fake.last_name()
email = f"{first_name.lower()}{random.randint(1000,9999)}@gmail.com"
password = ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*", k=12))

# Chrome options
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver", options=options)
wait = WebDriverWait(driver, 20)

try:
    driver.get("https://next.amboss.com/us/registration")

    wait.until(EC.presence_of_element_located((By.NAME, "email"))).send_keys(email)
    driver.find_element(By.NAME, "password").send_keys(password)

    sign_up_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//div[text()='Sign up']]")))
    driver.execute_script("arguments[0].click();", sign_up_button)

    country_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Country']")))
    country_input.send_keys("United States of America")
    time.sleep(1)
    country_input.send_keys(u'\ue007')
    time.sleep(1)

    next_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//div[text()='Next']]")))
    driver.execute_script("arguments[0].click();", next_btn)

    role_div = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[normalize-space(text())='Medical Student']")))
    driver.execute_script("arguments[0].click();", role_div)

    next_btn2 = wait.until(EC.presence_of_element_located((By.XPATH, "//button[.//div[text()='Next']]")))
    wait.until(lambda d: next_btn2.is_enabled() and next_btn2.get_attribute("aria-disabled") != "true")
    driver.execute_script("arguments[0].click();", next_btn2)

    university_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@aria-label='University']")))
    university_input.click()
    time.sleep(0.5)
    university_input.send_keys("Yale School of Medicine")
    time.sleep(1)
    university_input.send_keys(u'\ue007')

    grad_year_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@aria-label='Expected graduation year']")))
    grad_year_input.click()
    time.sleep(0.5)
    grad_year_input.send_keys("2026")
    time.sleep(1)
    grad_year_input.send_keys(u'\ue007')

    objective_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@aria-label='Current Objective']")))
    driver.execute_script("arguments[0].click();", objective_input)
    time.sleep(0.5)
    objective_input.send_keys("USMLE Step 2 CK")
    time.sleep(1)
    objective_input.send_keys(u'\ue007')

    driver.find_element(By.NAME, "firstName").send_keys(first_name)
    driver.find_element(By.NAME, "lastName").send_keys(last_name)

    checkbox_names = ["isBetaTester", "hasConfirmedPhysicianDisclaimer"]
    for name in checkbox_names:
        try:
            checkbox = driver.find_element(By.NAME, name)
            wrapper = checkbox.find_element(By.XPATH, "./ancestor::label | ./parent::*")
            if checkbox.get_attribute("aria-checked") != "true":
                driver.execute_script("arguments[0].click();", wrapper)
                time.sleep(0.3)
        except Exception:
            pass

    finish_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//div[text()='Finish set-up']]")))
    driver.execute_script("arguments[0].click();", finish_button)

    result = f"✅ Account created\n📧 Email: {email}\n🔐 Password: {password}"
    print(result)
except Exception as e:
    print(f"❌ Error: {str(e)}")
finally:
    driver.quit()
