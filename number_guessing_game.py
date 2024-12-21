import random
secret_number=random.randint(1,100)
guess=int(input("Enter a number :"))
if guess < secret_number:
    print("Too low!")
elif guess > secret_number:
    print("Too high!")
else:
    print("Congradulations! You guessed correct")
while guess !=secret_number:
    if guess < secret_number:
        print("Too high!")
    elif guess > secret_number:
        print("Too low!")
    #Ask for another guess
    guess=int(input("Guess again :"))
    #When the guess is made
    print("Congradulations! You guessed correct")
#Add limits to the attempt
attempt=0
max_attempt=5
#Adding while loop
while guess !=secret_number and max_attempt:
    attempts +=1
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    #Only ask if attempts remain
    if attempt < max_attempt:
        guess=int(input("Guess again :"))
    if secret_number==guess:
        print("Congradulations! You are correct")
    else:
        print("Sorry! Your attempts are over")


