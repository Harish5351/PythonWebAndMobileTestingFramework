from Features.Pages.Basepage import Basepage


class CalculatorIOSPage(Basepage):
    def __init__(self, context):
        Basepage.__init__(self, context.driver)
        self.context = context