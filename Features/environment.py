import json
import logging
import os
import time

from appium import webdriver
from allure_commons.types import AttachmentType
from allure_commons._allure import attach
from appium.options.common import AppiumOptions
from Features.Pages.Basepage import Basepage
from Features.Pages.CalculatorAndroidPage import CalculatorAndroidPage
from Features.Pages.CalculatorIOSPage import CalculatorIOSPage
from Features.Pages.FlipkartPage import FlipkartPage
from Features.Pages.FlipkartWebPage import FlipkartWebPage


def load_config_data():
    with open('Features/Resources/config.json', 'r') as f:
        return json.load(f)


def before_all(context):
    context.config_data = load_config_data()


def before_scenario(context, scenario):
    global tag
    tag = str(scenario.tags)
    if context.config_data["executionMode"] == "RealDevice":
        from appium import webdriver
        desired_cap = {
            "platformName": "Android",
            "platformVersion": context.config_data["androidVersion"],
            "deviceName": context.config_data["android_DeviceName"],
            "udid": context.config_data["android_udid"],  # Device UDID
            "appPackage": context.config_data["android_appPackage"],  # Path to the app file
            "appActivity": context.config_data["android_appActivity"],
            "automationName": context.config_data["android_automationName"],
            "ignoreHiddenApiPolicyError": True,
            "noReset": True,
            "newCommandTimeout": 300
        }
        url = 'http://127.0.0.1:4723/wd/hub'
        option = AppiumOptions().load_capabilities(desired_cap)
        context.driver = webdriver.Remote(command_executor=url, options=option)
    elif context.config_data["executionMode"] == "Web":
        from selenium import webdriver
        if context.config_data["browserName"] == "Chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--disable-cache")
            options.add_argument("--incognito")
            options.add_experimental_option("detach", True)
            preferences = {
                "profile.default_content_settings.popups": 0,
                "download.default_directory": os.getcwd() + os.path.sep + "Resources",
                "directory_upgrade": True
            }
            options.add_experimental_option('prefs', preferences)
            context.driver = webdriver.Chrome(options=options)
        elif context.config_data["browserName"] == "Edge":
            edge_options = webdriver.EdgeOptions()
            edge_options.use_chromium = True
            context.driver = webdriver.Edge(options=edge_options)
        else:
            logging.getLogger().error("Select the Valid Browser to execute TC e.g. Chrome or Edge")
    else:
        print("Driver initialization failed, cannot switch context or initialize page objects")

    # only for web testing
    context.driver.get(context.config_data["flipkart_URL"])
    context.driver.maximize_window()
    # only for mobile testing
    # context.driver.switch_to.context('NATIVE_APP')
    baseobject = Basepage(context.driver)
    context.android = CalculatorAndroidPage(baseobject)
    context.flipkart = FlipkartPage(baseobject)
    context.iOS = CalculatorIOSPage(baseobject)
    context.flipkartWeb = FlipkartWebPage(baseobject)
    context.stepid = 1


def after_scenario(context, scenario):
    if context.driver:
        # context.driver.reset()
        time.sleep(10)
        context.driver.quit()


def after_step(context, step):
    if context.driver:
        attach(context.driver.get_screenshot_as_png(), name=str(context.stepid), attachment_type=AttachmentType.PNG)
        context.stepid += 1
