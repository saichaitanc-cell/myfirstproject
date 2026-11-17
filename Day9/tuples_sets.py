#----TUPLES-----
limits = (11.5,14.8)
print(limits[0])
print(len(limits))
#limits[0]=12
#Unpacking: open the box into two variables
low,high = limits
print(f"Safe Range:{low}V to {high}V")
#----SETS-------
codes = ["P0301","P0420","P0301","P0171","P0420","P0301"]
unique = set(codes)
print(unique)
print(len(codes),"logged",len(unique),"unique")
print("unique list",unique)
unique.add("P0500")
unique.add("P0301")
#print("P0420" in unique)
print("updated unique",unique)#unique values can only be present.  
ordered =sorted(unique)
print(ordered[0])
#------SET MATH---
bench_a = {"P0301","P0420","P0171"}
bench_b = {"P0420","P0500","P0171"}

print(bench_a & bench_b)
print(bench_a | bench_b)
print(bench_a - bench_b)
