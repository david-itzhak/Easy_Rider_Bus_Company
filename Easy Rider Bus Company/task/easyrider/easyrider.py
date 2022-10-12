import json

json_string = input()
json_string = json_string.replace(" ", "")
json_list: list = json.loads(json_string)

errors = {"bus_id": 0,
          "stop_id": 0,
          "stop_name": 0,
          "next_stop": 0,
          "stop_type": 0,
          "a_time": 0
          }
for el in json_list:
    if not isinstance(el.get("bus_id"), int):
        errors["bus_id"] += 1
    if not isinstance(el.get("stop_id"), int):
        errors["stop_id"] += 1
    if not (isinstance(el.get("stop_name"), str) and len(el.get("stop_name")) > 0):
        errors["stop_name"] += 1
    if not isinstance(el.get("next_stop"), int):
        errors["next_stop"] += 1
    if not (isinstance(el.get("stop_type"), str) and len(el.get("stop_type")) < 2):
        errors["stop_type"] += 1
    if not (isinstance(el.get("a_time"), str) and len(el.get("a_time")) > 0):
        errors["a_time"] += 1

print("Type and required field validation:", sum(errors.values()))
for er, num in errors.items():
    print(f"{er}: {num}")
