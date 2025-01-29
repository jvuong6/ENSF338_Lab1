import os
import json
file_path = "large-file.json"
output_path = "output.2.3.json"
f = open(file_path, "r")
data = json.load(f)
for record in data:
    if "payload" in record and "size" in record["payload"]:
        record["payload"]["size"] = 42
data.reverse()
f = open(output_path, "w")
json.dump(data, f)