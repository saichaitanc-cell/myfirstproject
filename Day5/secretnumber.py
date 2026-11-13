import random
while True:                                                     #OUTER LOOP
    secret = random.randint(1,100)
    tries = 0
    print("\nNew game! I'm thinking of a number 1-100.")
    while True:#INNER LOOP
        guess = int(input("Guess the number: "))
        print(f"test code {secret}") #test code
        tries +=1
        if guess < secret:
            print(f"too low!")  
        elif guess > secret:
            print(f"too high!")
        else:
            print(f"you guessed the number in {tries} tries!")
            break                                               #INNER LOOP

    again = input("........")#"Play again? (y/n): "
    #if again !="y":
      #  print("Thanks for playing!")
        #break                                                  #OUTER LOOP
        