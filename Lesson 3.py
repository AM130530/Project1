print("💀 ULTIMATE GAMING QUIZ 💀")
print("Only true gamers can get 10/10!")
print("Answer using A, B, C or D.\n")

score = 0

answer = input("1. In Dark Souls, who fights alongside Ornstein?\nA) Artorias\nB) Smough\nC) Gwyn\nD) Sif\nAnswer: ").upper()

if answer == "B":
    print("Correct! 🔥\n")
    score += 1
else:
    print("Wrong! It was Smough. 💀\n")


answer = input("2. Which Minecraft enchantment launches you forward through water?\nA) Loyalty\nB) Impaling\nC) Riptide\nD) Channeling\nAnswer: ").upper()

if answer == "C":
    print("Correct! 🔥\n")
    score += 1
else:
    print("Wrong! It was Riptide. 💀\n")


answer = input("3. What is the name of the AI in Portal?\nA) SHODAN\nB) GLaDOS\nC) Cortana\nD) EDI\nAnswer: ").upper()

if answer == "B":
    print("Correct! 🔥\n")
    score += 1
else:
    print("Wrong! It was GLaDOS. 💀\n")


answer = input("4. Which studio created the original Half-Life?\nA) id Software\nB) Epic Games\nC) Valve\nD) Bungie\nAnswer: ").upper()

if answer == "C":
    print("Correct! 🔥\n")
    score += 1
else:
    print("Wrong! It was Valve. 💀\n")


answer = input("5. Which game features the character Master Chief?\nA) DOOM\nB) Halo\nC) Destiny\nD) Titanfall\nAnswer: ").upper()

if answer == "B":
    print("Correct! 🔥\n")
    score += 1
else:
    print("Wrong! It was Halo. 💀\n")


answer = input("6. Which studio developed Elden Ring?\nA) Capcom\nB) Ubisoft\nC) FromSoftware\nD) CD Projekt Red\nAnswer: ").upper()

if answer == "C":
    print("Correct! 🔥\n")
    score += 1
else:
    print("Wrong! It was FromSoftware. 💀\n")


answer = input("7. What is the name of the main villain in the original Portal?\nA) GLaDOS\nB) Wheatley\nC) Cave Johnson\nD) Gordon Freeman\nAnswer: ").upper()

if answer == "A":
    print("Correct! 🔥\n")
    score += 1
else:
    print("Wrong! It was GLaDOS. 💀\n")


answer = input("8. Which company created the Unreal Engine?\nA) Sony\nB) Epic Games\nC) Valve\nD) Nintendo\nAnswer: ").upper()

if answer == "B":
    print("Correct! 🔥\n")
    score += 1
else:
    print("Wrong! It was Epic Games. 💀\n")


answer = input("9. In Pokémon Red and Blue, where can you find Mewtwo?\nA) Mt. Moon\nB) Pokémon Tower\nC) Cerulean Cave\nD) Victory Road\nAnswer: ").upper()

if answer == "C":
    print("Correct! 🔥\n")
    score += 1
else:
    print("Wrong! It was Cerulean Cave. 💀\n")


answer = input("10. What does NPC stand for?\nA) New Player Control\nB) Non-Player Character\nC) Network Play Command\nD) Next Phase Challenge\nAnswer: ").upper()

if answer == "B":
    print("Correct! 🔥\n")
    score += 1
else:
    print("Wrong! It means Non-Player Character. 💀\n")


print("================================")
print("🏆 QUIZ FINISHED 🏆")
print("Your score:", score, "out of 10")

if score == 10:
    print("👑 LEGENDARY GAMER! UNSTOPPABLE!")
elif score >= 8:
    print("💎 ELITE GAMER!")
elif score >= 6:
    print("🔥 PRO GAMER!")
elif score >= 4:
    print("🎮 BEGINNER GAMER!")
elif score >= 1:
    print("🤡 YOU ARE A NOOB!")
else:
    print("💀 UR TERRIBLE!")

print("================================")