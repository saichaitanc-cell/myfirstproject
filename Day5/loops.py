readings = [12.6, 10.9, 15.2, 13.1, 35.0]
for voltage in readings:
    if voltage <11.5:
        print(f"{voltage} V: LOW ")
    elif voltage > 14.8:
        print(f"{voltage} V: OVER")
    else:
        print(f"{voltage} V: OK")

print("All readings checked")
#------------------------------------
for i in range(5):
    print(i)
for i in range(1,11):
    print(i)
for i in range(1,14,3):
    print(i)
#------------------------------------
count = 5
while count>0:
   print(f"Countdown: {count}")
   count -=1
print("Engine start")
#------------------------------------
list = [12.6, 13.0, 35.0, 12.8]
for vol in list:
    if vol > 30:
        print("sensor fault")
        break
    print(f"{vol} V Checked")
#------------------------------------
for volt in [12.6,-1,14.0]:
    if volt<0:
        continue
    print(f"{volt}V Checked")
