for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
#----------------------------------
password = input("Enter the passwords: ")
has_digit = False
for char in password:
    if char.isdigit():
        has_digit = True
long_enough = len(password) >= 8
#had_digit
if long_enough and has_digit:
    print("Strong password")
else:
    print("Weak password")
    if not long_enough:
        print("Password is too short")
    if not has_digit:
        print("No digit")