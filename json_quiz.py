import json
data={"a":2,"b":3}
js=json.dumps(data)
# json.dumps(data) converts the Python dictionary into a JSON formatted string.
parsed=json.loads(js)
# json.loads(js) converts the JSON string back into a Python dictionary.
parsed["c"]=parsed["a"]*parsed["b"]
# len(parsed) → Counts the number of keys in the dictionary → 3.
print(len(parsed),parsed["c"])
