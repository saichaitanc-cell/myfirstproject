readings=[0,1,2,3,4,5,6,7,8,9.1]
print(readings[0])
print(readings[-1])
print(readings[1:3])

readings[0]=0.1
print(readings)

readings.append(10)#add value at END
print(readings)
readings.insert(0,0.11)#add at position 0
readings.insert(5,0.55)#add at position 5##
print(readings)
readings.remove(3)
print(readings)
last=readings.pop()
print(f"poped value is:{last}")#detach the last value from list and store it in a variable
print(readings)
print(len(readings),min(readings),max(readings),sum(readings))
readings.sort()
print(readings)

for v in readings:
    print(f"{v}V")

if 9 in readings:
    readings.remove(9)
else:
    readings.insert(11,99)
print(readings)

low_readings = [] #empty list
for v in [12.8,10.3,11.2,13.8]:
    if v < 11.5:
        low_readings.append(v)

print(f"Low Readings:{low_readings}")

