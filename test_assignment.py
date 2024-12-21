from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

LAMBDA_TEST_USERNAME = "207006005"  
LAMBDA_TEST_ACCESS_KEY = "fcnFrfn6f9FhThtyWKp4bOP8CVDw3uiNz3GrkzngDNQneiM8p0"

# Konfigurasi LambdaTest
lt_options = {
    "browserName": "Chrome",
    "browserVersion": "latest",
    "platformName": "Windows 10",
    "selenium_version": "4.0.0",
    "username": LAMBDA_TEST_USERNAME,
    "accessKey": LAMBDA_TEST_ACCESS_KEY,
    "build": "Selenium Python 101",
    "name": "Sample Test",
}

chrome_options = Options()
chrome_options.set_capability("LT:Options", lt_options)

driver = webdriver.Remote(
    command_executor="https://hub.lambdatest.com/wd/hub",
    options=chrome_options
)

try:
    driver.get("https://lambdatest.github.io/sample-todo-app/")
    print("Berhasil membuka halaman")

    checkbox = driver.find_element(By.NAME, "li1")
    checkbox.click()
    print("Berhasil menandai item pertama")

    input_box = driver.find_element(By.ID, "sampletodotext")
    input_box.send_keys("Belajar Selenium dengan Python")
    input_box.send_keys(Keys.RETURN)
    print("Berhasil menambahkan item baru ke daftar")

    new_item = driver.find_element(By.XPATH, "//span[text()='Belajar Selenium dengan Python']")
    assert new_item.is_displayed(), "Item baru tidak ditemukan!"
    print("Berhasil memvalidasi item baru")

finally:
    driver.quit()
    print("Test selesai")
