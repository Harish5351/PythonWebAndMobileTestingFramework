import json
import os

class Locators:
    def __init__(self, filename):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, "../Resources/Locators", filename)
        self.data = self.load_json(file_path)

    def load_json(self, file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return {}

    def get_element_locator(self, locator_name):
        return self.data.get(locator_name, None)

# if __name__ == "__main__":
#     locator = Locators("Flipkart.json")
#     element_locator = locator.get_element_locator("button_name")
#     if element_locator:
#         print(f"Locator is: {element_locator}")
#     else:
#         print("Locator is not found.")
