from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from resources.locators_woffu import locator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
import time
import datetime
from sys import platform
import json

with open('resources/config.json') as file:
    data = json.load(file)

if platform == "linux" or platform == "linux2":
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(executable_path='usr/local/bin/chromedriver', options=options)
elif platform == "win32":
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome('driver/chromedriver_'+data['chromeDriverVersion'])

driver.get(locator.url)

def clocking():
    """
    This function is used to clock in.
    """
    action = "clocking"
    print("Starting "+action+" at "+__time_now())
    # __random_wait()
    login()
    iframe = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, locator.iframe))).get_attribute('src')
    driver.get(iframe)
    working_color = __get_day_color()
    if working_color == locator.workday_color:
        try:
            click_button()
            print(action+" at "+__time_now())
        except Exception as e:
            print("Error while "+action+" because "+str(e))
        finally:
            print(action+" at "+__time_now())
    else:
        print("Hoy no se trabaja champion xD")

    driver.quit()

def login():
    """
    This function is used to login to the woffu website.
    """
    try:
        __enter_credential(locator.user, locator.user_box, locator.siguiente_button)
        __enter_credential(locator.password, locator.pass_box, locator.iniciar_sesion_button)
    except Exception as e:
        print("Error while logging: "+str(e))
    finally:
        print("Login at "+__time_now())

def __enter_credential(key: str, box_path: str, button_path):
        """
        This function is used to enter credentials in the login page.

        Args:
            key (str): The key to enter in the box.
            box_path (str): The path to the box.
            button_path (_type_):
        """
        try:
            box = WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located((By.XPATH, box_path)))
            box.click()
            box.send_keys("caquita")
            button = WebDriverWait(driver, 15).until(
                    EC.element_to_be_clickable((By.XPATH, button_path)))
            button.click()
        except Exception as e:
            print("Error while entering credential: "+str(e))
            raise e

def click_button():
    """
    This function is used to click the button to clock in.
    """
    try:
        button_click = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, locator.button_clocking)))
        button_click.click()
    except Exception as e:
        print("Error while clicking button: "+str(e))

def __random_wait():
    """
    This function is used to wait a random time between 0 and 240 seconds.
    """
    seconds=random.randint(0, 240)
    time.sleep(seconds)

def __get_day_color() -> str:
    """
    This function is used to get the color of the day.
    Returns:
        str: The color of the day.
    """
    try:
        day_color = WebDriverWait(driver, 15).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, locator.day_color_element)))
        day_color = day_color.value_of_css_property('background-color')
        return day_color
    except Exception as e:
        print("Error while getting day color: "+str(e))
        return None

def __time_now() -> str:
    """
    This function is used to get the current time.
    Returns:
        str: The current time.
    """
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time