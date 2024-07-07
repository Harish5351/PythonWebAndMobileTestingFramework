import json
import os


class ReadJsonData:
    def __init__(self, filename):
        file_path = os.path.join("D:\\Unbox\\Features\\Resources\\TestData", filename)
        self.data = self.load_json(file_path)

    def load_json(self, file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return {}

    def get_value(self, key):
        return self.data.get(key, None)


# if __name__ == "__main__":
#     # Example usage
#     filename = "FlipkartData.json"
#     reader = ReadJsonData(filename)
#
#     # key = "cancel"
#     value = reader.get_value("Account")
#     print(value)
