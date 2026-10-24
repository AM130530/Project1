
import random

# Choose a secret number
secret_number = random.randint(1, 100)
attempts = 0

print("🎮 Welcome to Guess the Number!")
print("I'm thinking of a number between 1 and 100.")

while True:
    guess = input("Enter your guess: ")

    # Check whether the input is a number
    if not guess.isdigit():
        print("Please enter a valid whole number!")
        continue

    guess = int(guess)
    attempts += 1

    if guess < 1 or guess > 100:
        print("Choose a number between 1 and 100.")
    elif guess < secret_number:
        print("Too low! Try a bigger number.")
    elif guess > secret_number:
        print("Too high! Try a smaller number.")
    else:
        print(f"🎉 Correct! You won in {attempts} attempts!")
        break

print("Thanks for playing!")
