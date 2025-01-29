import os
import json
import timeit
input_file = "large-file.json"
output_file = "output.2.3.json"
f = open(input_file, "r")
if os.path.exists(output_file):
    os.remove(output_file)
data = json.load(f)

def modify_size():
    for record in data:
        if "payload" in record and "size" in record["payload"]:
            record["payload"]["size"] = 42
num_reps = 10
exec_time = timeit.timeit(modify_size, number = num_reps)
avg_time = exec_time / num_reps
data.reverse()
f = open(output_file, "w")
json.dump(data, f)
print(f"Average time to modify size in each record is {avg_time:.6f} seconds")