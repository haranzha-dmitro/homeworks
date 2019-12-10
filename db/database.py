import json

DB = {}

with open('db/test_data.json') as data:
    test_DB = json.load(data)
