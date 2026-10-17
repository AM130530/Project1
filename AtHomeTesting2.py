import random

print("============================")
print("💣 BOMB DEFUSER 💣")
print("============================")
print("The bomb is about to explode!")
print("Choose the correct wire!")
print("You have 3 attempts.\n")

secret_wire = random.choice(["red", "blue", "green"])
attempts = 3
defused = False

while attempts > 0:
    wire = input("Choose red, blue, or green: ").lower()

    if wire not in ["red", "blue", "green"]:
        print("That is not a valid wire!\n")
        continue

    if wire == secret_wire:
        print("🎉 BOOM... just kidding! Bomb defused!")
        print("🏆 YOU ARE A HERO!")
        defused = True
        break
    else:
        attempts -= 1
        print("Wrong wire! The bomb is ticking...")
        print("Attempts left:", attempts, "\n")

if not defused:
    print("💥 BOOM! GAME OVER!")
    print("The correct wire was", secret_wire)

print("Thanks for playing! 🎮")