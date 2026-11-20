#dictionary
readings = {"WS01": 45.2, "OT02": 98.5, "VM03": 12.6,"VM03": 111}

print(readings["OT02"])
print(len(readings))

#Add,change,delete
readings["LP04"]=3.3 #ADD
readings["VM03"]=13.1 #change
del readings["WS01"]
print(readings)

#Safelookup
#print(readings["XX99"]) #leads to crash
print(readings.get("XX99")) #no crash results NONE
print(readings.get("XX99",5.5)) # XX99 is not in readings dictionary, so it returns your own default value
print("OT02" in readings) # TRUE Check the keys

#LOOP
for sensor, value in readings.items():
    print(f"{sensor}:{value}")

print(list(readings.keys()))  #Just the names
print(list(readings.values()))  #just the values

#print(readings.keys())  #Just the names, outputs dict_keys(['OT02', 'VM03', 'LP04'])
#print(readings.values())  #just the values, outputs dict_values([98.5, 13.1, 3.3])

