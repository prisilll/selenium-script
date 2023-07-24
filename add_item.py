from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Inisialisasi WebDriver
driver = webdriver.Chrome()

# Buka halaman login
driver.get("https://www.saucedemo.com/")

# Login dengan kredensial valid
username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

username.send_keys("standard_user")
password.send_keys("secret_sauce")
login_button.click()

# Tambahkan item ke dalam keranjang belanja
item_add_button = driver.find_element(By.XPATH, "//div[@class='inventory_item'][1]//button")
item_add_button.click()

# Verifikasi apakah item berhasil ditambahkan ke dalam keranjang belanja
time.sleep(3)  # Tunggu beberapa detik agar halaman benar-benar terload
cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
assert cart_badge.text == "1"

# Tutup browser
driver.quit()
