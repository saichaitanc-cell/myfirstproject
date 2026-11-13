temp = float(input("Enter the temperature: "))
speed = int(input("Enter the speed value: "))
door_open = True
if temp > 120:
    print("OVERHEAT - reduce power!")
elif temp >100:
    print("WARNING - running hot")
else:
    print("Temperature OK")

print("Check Complete")

if speed == 0 and door_open:
    print("Safe:Car stopped, door open")
elif speed>120 or door_open:
    print("Alert!")
     
