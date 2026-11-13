#number = int(input("Enter a number: "))
#for i in range(1, 11):
#    print(f"{number} * {i} = {number*i}")
#----------------------
import random
secret = random.randint(1,100)
print(f"secret number is {secret}") #test code
tries = 0
while True:
    guess = int(input("Guess the number: "))
    tries +=1   
    if guess < secret:
        print(f"too low!")
    elif guess > secret:
        print(f"too high!")
    else:
        print(f"you guessed the number in {tries} tries!")
        break

