import json
from validation_funcs import validate_time_format, validate_stop_name

json_string = input()
json_list: list = json.loads(json_string)

# errors = {"bus_id": 0,
#           "stop_id": 0,
#           "stop_name": 0,
#           "next_stop": 0,
#           "stop_type": 0,
#           "a_time": 0
#           }
errors = {
          "stop_name": 0,
          "stop_type": 0,
          "a_time": 0
          }
bus_lines_dict: dict = {}

for el in json_list:
    # if not isinstance(el.get("bus_id"), int):
    #     errors["bus_id"] += 1
    # if not isinstance(el.get("stop_id"), int):
    #     errors["stop_id"] += 1
    if not (isinstance(el.get("stop_name"), str) and validate_stop_name(el.get("stop_name"))):
        errors["stop_name"] += 1
    # if not isinstance(el.get("next_stop"), int):
    #     errors["next_stop"] += 1
    if not (isinstance(el.get("stop_type"), str) and len(el.get("stop_type")) < 2 and el.get("stop_type") in ["", "O", "S", "F"]):
        errors["stop_type"] += 1
    if not (isinstance(el.get("a_time"), str) and len(el.get("a_time")) > 0 and validate_time_format(el.get("a_time"))):
        errors["a_time"] += 1

    if el.get("bus_id") not in bus_lines_dict:
        bus_lines_dict[el.get("bus_id")] = 1
    else:
        bus_lines_dict[el.get("bus_id")] += 1

# print("Format validation:", sum(errors.values()), "errors")
# for er, num in errors.items():
#     print(f"{er}: {num}")

print("Line names and number of stops:")
for bus_id, stops_number in bus_lines_dict.items():
    print(f'bus_id: {bus_id}, stops: {stops_number}')
