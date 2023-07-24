from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inisialisasi WebDriver (Google Chrome)
driver = webdriver.Chrome()

try:
    # Buka halaman https://www.saucedemo.com/
    driver.get("https://www.saucedemo.com/")

    # Masukkan username dan password untuk login
    username = "standard_user"
    password = "secret_sauce"

    # Dapatkan elemen kotak username dan password
    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")

    # Masukkan username dan password
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Klik tombol login
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    # Tunggu hingga halaman produk selesai dimuat
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )

    # Dapatkan daftar produk yang tersedia
    products = driver.find_elements(By.CLASS_NAME, "inventory_item_name")

    # Cetak nama produk yang tersedia
    print("Daftar Produk yang Tersedia:")
    for product in products:
        print(product.text)

except Exception as e:
    print("Terjadi kesalahan:", e)

finally:
    # Tutup browser setelah selesai
    driver.quit()
