while True:
    choice = input("Choose (+ - * / or q to quit): ")
    if choice == "q":
        print("Goodbye!")
        break
    if choice not in ("+", "-", "*", "/" or "q to quit"):
        print("Invalid input")
        continue
    first_num = float(input("Enter the first number: "))
    second_num = float(input("Enter the second number: "))
    if choice == "+":
        print(f"{first_num} + {second_num} = {first_num + second_num}")
    elif choice == "-":
        print(f"{first_num} - {second_num} = {first_num - second_num}")
    elif choice == "*":
        print(f"{first_num} * {second_num} = {first_num * second_num}")
    elif choice == "/":
        if second_num != 0:
            print(f"{first_num} / {second_num} = {first_num / second_num}")
        else:
            print("Cannot divide by zero!")
    
