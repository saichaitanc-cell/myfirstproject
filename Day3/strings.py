#name = "SAI CHAITANYA"
#print("1st letter: ",name[0])
#print("Last letter: ",name[-1])

#print(name[0:3])
#print(name[4:13]) #from 4 to last 
#print(name[:4])#start till n-1
#print(name[4:])#n till end

#name=name.lower()
#print(name)
#print(name.upper())
#parts = name.split()
#print("Parts: ", parts)


name = input("Enter your full name: ")
title_name = name.title() 
print("Name: ", title_name)
parts = title_name.split()
for word in parts:
    print(f"{word[0]}. ", end=".")
#print(f"Initials: {parts[0][0]}. {parts[1][0]}. {parts[2][0]}")
print("Reversed: ", name[::-1])
print(f"Length: {len(name)}")
print("   ")
print(f"{"sai"} {"chaitanya"}")
value = 2.04839238
print(f"{"value is "}: {value:.2f}")


