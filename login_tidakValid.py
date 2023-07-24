from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Inisialisasi WebDriver
driver = webdriver.Chrome()

# Buka halaman login
driver.get("https://www.saucedemo.com/")

# Input kredensial tidak valid
username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

username.send_keys("invalid_user")
password.send_keys("wrong_password")
login_button.click()

# Verifikasi apakah login gagal dengan mengecek adanya pesan error
time.sleep(3)  # Tunggu beberapa detik agar halaman benar-benar terload
error_message = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
assert error_message.text == "Epic sadface: Username and password do not match any user in this service"

# Tutup browser
driver.quit()
