voltage = float(input("Enter battery voltage: "))

if not (0 <= voltage <= 30):#if (0 <= voltage) and (voltage <= 30): 
    print(f"{voltage:.2f} V: Invalid reading - sensor fault")
elif voltage < 11.5:
    print(f"{voltage:.2f} V: LOW_VOLTAGE - check battery")
elif voltage > 14.8:
    print(f"{voltage:.2f} V: OVER_VOLTAGE - check alternator")
else:
    print(f"{voltage:.2f} V: Voltage OK")

