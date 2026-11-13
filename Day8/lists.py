readings=[0,1,2,3,4,5,6,7,8,9]
print(readings[0])
print(readings[-1])
print(readings[1:3])

readings[0]=0.1
print(readings)

readings.append(10)#add value at END
print(readings)
readings.insert(0,0.11)#add at position 0
readings.insert(5,0.55)#add at position 5#
print(readings)
readings.remove(3)
print(readings)
last=readings.pop()
print(f"poped value is:{last}")
print(readings)
print(len(readings),min(readings),max(readings),sum(readings))
readings.sort()
print(readings)

for v in readings:
    print(f"{v}V")


