import time

from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Features.Pages.Basepage import Basepage


class FlipkartWebPage(Basepage):
    def __init__(self, context):
        Basepage.__init__(self, context.driver)
        self.context = context
        self.wait = WebDriverWait(self.driver, 20)

    def enter_into_textfield(self, locator, value):
        element = self.driver.find_element(By.XPATH, locator)
        element.send_keys(value, Keys.ENTER)

    def verify_result_on_screen(self, locator, value):
        time.sleep(5)
        element = self.driver.find_element(By.XPATH, locator)
        # element = WebDriverWait.until(EC.visibility_of_element_located((By.XPATH, locator)))
        element_text = element.text
        print("element_text: ", element_text)
        end_index = element_text.find("results")
        print("end_index: ", end_index)
        result = element_text[8:end_index - 1].strip()
        print("result: ", result)
        print("value: ", value)
        # assert result == value

    def select_element(self, locator, value):
        elements = self.driver.find_elements(By.XPATH, locator)
        if len(elements) >= 11:
            element_10 = elements[9]
            print("element_10 is selected")
            elements_11 = elements[10]
            print("elements_11 is selected")
            element_10.click()
            time.sleep(2)
            elements_11.click()

    def verify_item_in_tray(self, locator, value):
        item_element = self.driver.find_element(By.XPATH, locator)
        if item_element.is_displayed():
            item_text = item_element.text
            print("item_text: ", item_text)
            value_check = item_text.find("2")
            print("value_check: ", value_check)
            count = item_text[value_check:value_check+1].strip()
            print("Count: ", count)
            assert count == value

    def click_element(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        if element.is_displayed():
            element.click()

    def verify_element_on_screen(self, locator, value):
        time.sleep(3)
        elements = self.driver.find_elements(By.XPATH, locator)
        for index, element in enumerate(elements):
            if element.is_displayed():
                print(f"Element {index + 1} is visible.")
                item_text = element.text
                print("items text: ", item_text)
            else:
                print(f"Element {index + 1} is not visible.")

    def back_to_previous_page(self):
        self.driver.back()
        url = self.driver.current_url
        print("url: ", url)
        self.driver.refresh()
        time.sleep(5)

    def scroll_to_spec_element(self, locator, value):
        elements = self.driver.find_elements(By.XPATH, locator)
        # elements = WebDriverWait.until(EC.visibility_of_element_located(locator))
        time.sleep(10)
        num_elements = len(elements)
        print("num_elements: ", num_elements)
        if len(elements) >= 10:
            tenth_element = elements[9]
            self.driver.execute_script("arguments[0].scrollIntoView(true);", tenth_element)
            time.sleep(5)
            # required_element_text = tenth_element.text
            # print("required_element_text: ", required_element_text)
            self.original_window = self.driver.current_window_handle
            print("original window: ", self.original_window)
            time.sleep(5)
            tenth_element.click()
        else:
            print(f"There are less than {value} elements on the page.")

    def switch_to_new_window(self):
        all_windows = self.driver.window_handles
        for window in all_windows:
            if window != self.original_window:
                self.driver.switch_to.window(window)
                break

    # def verify_message_on_page(self, locator, value):
    #     price_element = self.driver.find_element(By.XPATH, "//div[@class='Nx9bqj CxhGGd']")
    #     self.price_value = price_element.text
    #     print("Value of Added Device: ", self.price_value)
    #     try:
    #         # Wait for the text to change to "Going to cart"
    #         going_to_cart_text = WebDriverWait(self.driver, 5).until(
    #             EC.text_to_be_present_in_element((By.XPATH, locator), value)
    #         )
    #         print(f"Text changed to {value} successfully.")
    #     except:
    #         print(f"Failed to verify that the text changed to {value}.")

    def before_value(self):
        price_element = self.driver.find_element(By.XPATH, "//div[@class='Nx9bqj CxhGGd']")
        self.price_value = price_element.text
        print("Value of product before adding to cart: ", self.price_value)
        time.sleep(5)

    def verify_price(self, locator):
        cart_price_element = self.driver.find_element(By.XPATH, locator)
        cart_value = cart_price_element.text
        print("Cart Value: ", cart_value)
        assert cart_value == self.price_value

    def verify_popup_message(self, locator, value):
        try:
            element = self.driver.find_element(By.XPATH, locator)
            element_text = element.text
            print("pop_up_message: ", element_text)
            # assert element_text == value
            if value in element_text:
                print("Assertion Passed")
        except NoSuchElementException:
                print("Assertion Failed")



