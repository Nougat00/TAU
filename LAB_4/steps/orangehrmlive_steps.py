from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import logging

logger = logging.getLogger('selenium')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

driver = None


@given('I am on the orangehrmlive.com login page')
def step_open_orangehrmlive(context):
    global driver
    driver = webdriver.Chrome()
    logger.info("Opening orangehrmlive.com")
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.implicitly_wait(2)

@when('I enter username: "{username}" and password: "{password}"')
def step_enter_orangehrm_credentials(context, username, password):
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)

@when('I click login button')
def step_click_orangehrm_login(context):
    driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
    driver.implicitly_wait(2)

@then('I should be logged in successfully to orangehrmlive.com')
def step_check_orangehrm_login_success(context):
    try:
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[1]/div[1]/i")
        logger.info("Successfully logged in")
    except Exception as e:
        logger.error(f"Failed to log in: {e}")
        driver.close()

@then('I change my username to "{new_username}"')
def step_change_username(context, new_username):
    try:
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a").click()
        driver.implicitly_wait(2)
        lastNameInput = driver.find_element(By.NAME, "lastName")
        lastNameInput.send_keys(Keys.CONTROL + "a")
        lastNameInput.send_keys(Keys.BACKSPACE)
        lastNameInput.send_keys(new_username)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button").click()
        driver.implicitly_wait(2)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a").click()
        driver.implicitly_wait(2)
        assert new_username in driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p").text
        logger.info("Successfully changed username")
    except Exception as e:
        logger.error(f"Failed to change username: {e}")
    finally:
        driver.close()