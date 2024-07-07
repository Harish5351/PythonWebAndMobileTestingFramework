from behave import *
from Features.Utils.Locators import Locators
from Features.Utils.ReadJsonData import ReadJsonData
element_locator = Locators("Flipkart.json")
test_data = ReadJsonData("FlipkartData.json")
use_step_matcher("parse")

@when('User clicks on "{button_name}" button')
def user_clicks_on_number(context, button_name):
    locator = element_locator.get_element_locator(button_name)
    value = test_data.get_value(button_name)
    context.flipkart.tap_button(locator, value)

@when('User clicks on x button')
def user_click_x():
    locator = element_locator.get_element_locator()
