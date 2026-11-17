sensor_ids= ["WS01", "OT02", "WS01", "VM03", "OT02", "WS01", "LP04"]
print(f"Total logged: {len(sensor_ids)}")
sensor_val=set(sensor_ids)
print(f"Unique sensors: {len(sensor_val)}")
sorted_val = sorted(sensor_val)
print(f"Sorted: {sorted_val}")
print(f"Duplicates removed: {len(sensor_ids)-len(sensor_val)}")
bench_1 = ["WS01", "OT02", "VM03", "LP04"]
bench_2 = ["OT02", "LP04", "TP05", "WS01", "RP06"]
set_1 = set(bench_1)
set_2 = set(bench_2)
print(f"On both benches: {set_1 & set_2}")
print(f"Only on bench 1: {set_1 - set_2}")
print(f"Only on bench 2: {set_2 - set_1}")
print("All sensors: ",sorted(set_1 | set_2))
oil_limits = (100,120)
warn, overheat = oil_limits
for temp in [80,100,112,120,130]:
    if temp > overheat:
       print(f"{temp} C: OVERHEAT")
    elif temp > warn:
       print(f"{temp} C: WARNING")
    else:
       print("OK")
