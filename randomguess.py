import random
def hint_by_me(guess, secret):
    if guess > secret:
        return "Too high!"
    else:
        return "Too low!"
while True:
    secret_number = random.randint(1, 50)
    attempts = 0
    print("I have selected a number between 1 and 50.")
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1
        if guess == secret_number:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break
        else:
            print(hint_by_me(guess, secret_number))
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing!!!!")
        break
    #adding a comment 