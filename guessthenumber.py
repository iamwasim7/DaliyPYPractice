#Number guessing game 
#Create a program where the computer has a fixed secret number.
#The user keeps guessing until they get it correct.


secret_number = 25

while True:
    guess = int(input("Guess the number: "))

    if guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Correct! 🎯")
        break