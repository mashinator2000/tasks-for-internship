# Задание 3: report.json

import json
with open('fortest/tests.json', 'r') as file:
    data = json.load(file)
data = data["tests"]
print(data[0]["title"])