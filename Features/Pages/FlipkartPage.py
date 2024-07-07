from selenium.common import NoSuchElementException, InvalidSelectorException
from selenium.webdriver.common.by import By

from Features.Pages.Basepage import Basepage
import json
data = json.load(open("Features/Resources/Locators/Flipkart.json"))
from Features.Utils.Locators import Locators
locator = Locators("Flipkart.json")
class FlipkartPage(Basepage):
    def __init__(self, context):
        Basepage.__init__(self, context.driver)
        self.context = context

    def tap_button(self, locator, value):
        try:
            element = self.driver.find_element(By.XPATH, locator.replace("replace_text", value))
            element.click()
        except NoSuchElementException:
            element = self.driver.find_element(By.XPATH, locator)
            element.click()
        # try:
        #     option = data["button_name"]
        #     element = self.driver.find_element(By.XPATH, option.replace("replace_text", button_name))
        #     element.click()
        # except (NoSuchElementException, InvalidSelectorException):
        #     option = data["cancel"]
        #     element = self.driver.find_element(By.ID, option)
        #     element.click()
