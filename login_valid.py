from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Inisialisasi WebDriver
driver = webdriver.Chrome()

# Buka halaman login
driver.get("https://www.saucedemo.com/")

# Input kredensial valid
username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

username.send_keys("standard_user")
password.send_keys("secret_sauce")
login_button.click()

# Verifikasi apakah login berhasil dengan mengecek URL baru setelah login
time.sleep(3)  # Tunggu beberapa detik agar halaman benar-benar terload
assert "inventory" in driver.current_url

# Tutup browser
driver.quit()
