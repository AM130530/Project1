
import random

words = ["python", "computer", "elephant", "school", "gaming"]

secret_word = random.choice(words)
guessed_letters = []
attempts_left = 6

print("🎮 WELCOME TO THE WORD GUESSING GAME!")
print("Guess the secret word one letter at a time.")
print("You have 6 incorrect guesses available.")

while attempts_left > 0:
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Attempts left:", attempts_left)

    if all(letter in guessed_letters for letter in secret_word):
        print("🎉 Congratulations! You guessed the word!")
        break

    guess = input("Guess a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter just one letter!")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Great! That letter is in the word.")
    else:
        attempts_left -= 1
        print("❌ Wrong letter!")

else:
    print("\n😢 Game over!")
    print("The secret word was:", secret_word)

print("Thanks for playing! 👋")
