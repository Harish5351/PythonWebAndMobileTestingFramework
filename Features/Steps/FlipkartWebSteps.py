from behave import *
from Features.Utils.Locators import Locators
from Features.Utils.ReadJsonData import ReadJsonData

element_locator = Locators("FlipkartWeb.json")
test_data = ReadJsonData("FlipkartWebData.json")
use_step_matcher("parse")


@when('User enters "{text}" into text field')
def user_enters_text_into_text_field(context, text):
    locator = element_locator.get_element_locator(text)
    print("locator: ", locator)
    value = test_data.get_value(text)
    context.flipkartWeb.enter_into_textfield(locator, value)


@then('User verifies "{result}" displayed')
def verify_result_displayed_on_screen(context, result):
    locator = element_locator.get_element_locator(result)
    value = test_data.get_value(result)
    context.flipkartWeb.verify_result_on_screen(locator, value)


@when('User clicks on "{element}" of page to compare elements')
def user_compares_element(context, element):
    locator = element_locator.get_element_locator(element)
    value = test_data.get_value(element)
    context.flipkartWeb.select_element(locator, value)


@then('User verifies "{item}" in tray')
def user_verifies_item_in_tray(context, item):
    locator = element_locator.get_element_locator(item)
    value = test_data.get_value(item)
    context.flipkartWeb.verify_item_in_tray(locator, value)


@when('User clicks "{element}" on page')
def user_enters_text_into_text_field(context, element):
    locator = element_locator.get_element_locator(element)
    # value = test_data.get_value(element)
    context.flipkartWeb.click_element(locator)


@then('User verifies "{Items}" displayed on screen')
def user_verifies_elements_on_screen(context, Items):
    locator = element_locator.get_element_locator(Items)
    value = test_data.get_value(Items)
    context.flipkartWeb.verify_element_on_screen(locator, value)


@when("User navigates back to the previous page")
def user_navigates_back_to_previous_page(context):
    context.flipkartWeb.back_to_previous_page()


@when('User scroll down to "{element}" element')
def user_scroll_to_element(context, element):
    locator = element_locator.get_element_locator(element)
    value = test_data.get_value(element)
    context.flipkartWeb.scroll_to_spec_element(locator, value)


@when('User navigates to product description window')
def user_navigates_new_window(context):
    context.flipkartWeb.switch_to_new_window()


@then('User verifies "{message}" message on page')
def user_verifies_message_on_page(context, message):
    locator = element_locator.get_element_locator(message)
    value = test_data.get_value(message)
    context.flipkartWeb.verify_message_on_page(locator, value)


@then('User verifies "{values}" are the same before and after adding to the cart')
def user_verifies_before_after_value(context, values):
    locator = element_locator.get_element_locator(values)
    # value = test_data.get_value(values)
    context.flipkartWeb.verify_price(locator)


@then('User verifies popup message "{popup_message}" displayed on screen')
def user_verifies_popup_message(context, popup_message):
    locator = element_locator.get_element_locator(popup_message)
    value = test_data.get_value(popup_message)
    context.flipkartWeb.verify_popup_message(locator, value)


@when('User capture price of product')
def user_capture_value(context):
    context.flipkartWeb.before_value()
