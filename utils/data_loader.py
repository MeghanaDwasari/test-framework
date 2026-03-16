import json

def load_test_data():

    with open("config/test_data.json") as f:
        return json.load(f)