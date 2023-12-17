from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging

logger = logging.getLogger('selenium')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

driver = None


@given(u'I am on the saucedemo.com login page')
def step_open_saucedemo(context):
    global driver
    driver = webdriver.Chrome()
    logger.info("Otwieranie serwisu saucedemo.com")
    driver.get("https://www.saucedemo.com/")


@when('I enter username "{username}" and password "{password}"')
def step_enter_credentials(context, username, password):
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)


@when('I click the login button')
def step_click_login(context):
    driver.find_element(By.ID, "login-button").click()
    driver.implicitly_wait(2)


@then('I should be logged in successfully')
def step_check_login_success(context):
    try:
        driver.find_element(By.ID, "shopping_cart_container")
        logger.info("Logowanie do serwisu przebiegło pomyślnie")
    except:
        logger.error("Nie udało zalogować się do serwisu")
        driver.close()


@then('I add products to the cart')
def step_add_products_to_cart(context):
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    if 3 == driver.find_element(By.CLASS_NAME, "shopping_cart_container").text:
        logger.info("Test przeszedł pomyślnie")
    else:
        logger.error("Błąd podczas dodawania produktów do koszyka")
    driver.close()
