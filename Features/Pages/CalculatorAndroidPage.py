from selenium.webdriver.common.by import By

from Features.Pages.Basepage import Basepage


class CalculatorAndroidPage(Basepage):
    def __init__(self, context):
        Basepage.__init__(self, context.driver)
        self.context = context

    def tap_number(self, number):
        num = self.driver.find_element(By.ID, "com.miui.calculator:id/btn_"+number+"_s")
        num.click()

    def tap_operator(self, opt):
        operator = self.driver.find_element(By.ID, "com.miui.calculator:id/btn_"+opt+"_s")
        operator.click()

    def verify_answer(self, ans):
        answer = self.driver.find_element(By.ID, "com.miui.calculator:id/result")
        answer_text = answer.text
        print(answer_text)
        result = answer_text[2:].strip()
        # result = answer_text[2:]
        print("result: " +result)
        assert result == ans