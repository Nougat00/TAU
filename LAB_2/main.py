from selenium import webdriver
import logging

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

logger = logging.getLogger('selenium')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

driver = webdriver.Chrome()
logger.info("Otwieranie serwisu saucedemo.com")
driver.get("https://www.saucedemo.com/")
logger.info("Logowanie do serwisu")
driver.find_element(By.ID, "user-name").send_keys("problem_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
driver.implicitly_wait(2)
try:
    driver.find_element(By.ID, "shopping_cart_container")
    logger.info("Logowanie do serwisu przebiegło pomyślnie")
except:
    logger.error("Nie udało zalogować się do serwisu")
    driver.close()
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
if 3 == driver.find_element(By.CLASS_NAME, "shopping_cart_container").text:
    logger.info("Test przeszedł pomyślnie")
else:
    logger.error("Błąd podczas dodawania produktów do koszyka")

driver.close()

driver = webdriver.Edge()
logger.info("Otwieranie serwisu orangehrmlive.com")
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(2)
logger.info("Logowanie do serwisu")
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
driver.implicitly_wait(2)
try:
    driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[1]/div[1]/i")
except:
    logger.error("Nie udało zalogować się do serwisu")
    driver.close()
logger.info("Test zmiany nazwiska uzytkownika")
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a").click()
driver.implicitly_wait(2)
lastNameInput = driver.find_element(By.NAME, "lastName")
lastNameInput.send_keys(Keys.CONTROL + "a")
lastNameInput.send_keys(Keys.BACKSPACE)
lastNameInput.send_keys("Tester")
driver.find_element(By.XPATH,
                    "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button").click()
driver.implicitly_wait(2)
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a").click()
driver.implicitly_wait(2)
if driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p").text.find("Tester"):
    logger.info("Zmiana nazwy użytkownika przebiegła pomyślnie")
else:
    logger.error("Błąd podczas zmiany nazwy użytkownika")

driver.close()