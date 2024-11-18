import json

def print_response(response):
    data = response.json()
    json_string = json.dumps(data)
    print(json_string)

def create_file(name, location, value):
    f = open(location + name, "a")
    f.write(value)
    f.close()