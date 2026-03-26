import json
file = open("users.json", "r")
data = file.read()
items = json.loads(data)
print(items)