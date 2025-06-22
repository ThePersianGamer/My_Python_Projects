import random
user_guess =  int(input("Guess a number between 1-10."))
computer_guess = random.randint(1, 10)
attempt = 1
while True:
    if user_guess == computer_guess:
        print("You've guessed right!")
        break
    else:
        print("You haven't guessed right.")
        user_guess = int(input("Guess a number between 1-10."))
    attempt += 1
    if attempt == 3:
        print("You reached the limit")