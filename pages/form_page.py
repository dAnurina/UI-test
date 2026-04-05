import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FormPage:
    URL = "https://practice-automation.com/form-fields/"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # --- locators ---
    NAME = (By.ID, "name-input")
    PASSWORD = (By.XPATH, "//input[@type='password']")
    MILK = (By.ID, "drink2")
    COFFEE = (By.CSS_SELECTOR, "#drink3")
    YELLOW = (By.ID, "color3")
    AUTOMATION = (By.ID, "automation")
    EMAIL = (By.ID, "email")
    MESSAGE = (By.ID, "message")
    SUBMIT = (By.ID, "submit-btn")

    # --- actions (Fluent style) ---
    def open(self):
        self.driver.get(self.URL)
        return self

    def enter_name(self, name):
        self.driver.find_element(*self.NAME).send_keys(name)
        return self

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        return self

    def select_drinks(self):
        self.click(self.MILK)
        self.click(self.COFFEE)
        return self

    def select_color(self):
        self.click(self.YELLOW)
        return self

    def select_automation(self):
        select = Select(self.driver.find_element(*self.AUTOMATION))
        select.select_by_value("yes")
        return self

    def enter_email(self, email):
        self.driver.find_element(*self.EMAIL).send_keys(email)
        return self

    def enter_message(self):
        tools = ["Selenium", "Playwright", "Cypress", "Appium", "Katalon Studio"]

        count = len(tools)
        longest = max(tools, key=len)

        text = f"{count} tools. Longest: {longest}"

        self.driver.find_element(*self.MESSAGE).send_keys(text)
        return self

    def submit(self):
        self.click(self.SUBMIT)
        return self

    def get_alert_text(self):
        alert = self.wait.until(EC.alert_is_present())
        text = alert.text

        time.sleep(3)  # 👈 чтобы увидеть алерт

        alert.accept()
        return text
    
    def click(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))

        # скроллим в центр (ВАЖНО — не true!)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )

        # ждём, пока станет кликабельным
        element = self.wait.until(EC.element_to_be_clickable(locator))

        try:
            element.click()
        except:
            # fallback через JS (как делают в проде)
            self.driver.execute_script("arguments[0].click();", element)