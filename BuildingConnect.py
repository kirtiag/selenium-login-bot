import os,time,random,sys
try:
    from selenium import webdriver
except ImportError:
    print("Selenium not found. Installing...")
    os.system("pip install selenium")
    from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

import Crentials

email     = Crentials.Email
password  = Crentials.password

chrome_options = ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) " + "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119 Safari/537.36")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.maximize_window()
wait = WebDriverWait(driver, 15)
try:
    
    driver.get("https://app.buildingconnected.com/logout")
    time.sleep(2)
    driver.delete_all_cookies()
    driver.execute_script("window.localStorage.clear();")
    driver.execute_script("window.sessionStorage.clear();")
    driver.get('https://app.buildingconnected.com/login')
    wait.until(EC.presence_of_element_located((By.ID, "emailField"))).send_keys(email)
    time.sleep(random.uniform(2, 5))
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="NEXT"]'))).click()
    time.sleep(random.uniform(2, 5))
    wait.until(EC.element_to_be_clickable((By.XPATH, '//span[@class="button-text"]'))).click()
    time.sleep(random.uniform(2, 5))
    wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys(password)
    time.sleep(random.uniform(2, 5))
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))).click()
    time.sleep(random.uniform(2, 5))
    
    code = input("Enter verification code: ")
    wait.until(EC.presence_of_element_located((By.NAME, "VerificationCode"))).send_keys(code)
    time.sleep(random.uniform(2, 5))
    wait.until(EC.element_to_be_clickable((By.ID, "btnSubmit"))).click()
    time.sleep(random.uniform(2, 5))
    print("Logged in successfully...")
    
except (TimeoutException, NoSuchElementException) as e:
        driver.save_screenshot("failure.png")
        driver.quit()
        print("Login or extraction failed:", e)
        sys.exit(1)

except Exception as e:
    driver.save_screenshot("error.png")
    driver.quit()
    print("Unexpected error:", e)
    sys.exit(1)
finally:
    print("Logging out...")
    driver.get("https://app.buildingconnected.com/logout")
    time.sleep(random.uniform(2, 5))
    driver.quit()
    print("Session ended.")    