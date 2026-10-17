print("=" * 45)
print("          THE ULTIMATE GAMING QUIZ")
print("=" * 45)
print("Welcome, gamer!")
print("There are 10 multiple-choice questions.")
print("Choose A, B, C or D for each question.")
print("Each correct answer earns 1 point.")
print("=" * 45)

questions = [
    {
        "game": "Minecraft",
        "difficulty": "Easy",
        "question": "Which mob explodes when it gets close to you?",
        "options": [
            "A. Zombie",
            "B. Creeper",
            "C. Skeleton",
            "D. Enderman"
        ],
        "answer": "B",
        "explanation": "Creepers explode when they get close enough!"
    },
    {
        "game": "Fortnite",
        "difficulty": "Easy",
        "question": "What is the main objective in Fortnite Battle Royale?",
        "options": [
            "A. Build the biggest house",
            "B. Collect every weapon",
            "C. Be the last player or team standing",
            "D. Score the most football goals"
        ],
        "answer": "C",
        "explanation": "The goal is to survive until you or your team wins."
    },
    {
        "game": "EA Sports FC",
        "difficulty": "Easy",
        "question": "How many players from one team start a normal "
                    "11-a-side football match on the pitch?",
        "options": [
            "A. 9",
            "B. 10",
            "C. 11",
            "D. 12"
        ],
        "answer": "C",
        "explanation": "A team starts with 11 players, including the goalkeeper."
    },
    {
        "game": "GTA V",
        "difficulty": "Easy",
        "question": "Which city is the main setting of GTA V?",
        "options": [
            "A. Liberty City",
            "B. Los Santos",
            "C. Vice City",
            "D. San Fierro"
        ],
        "answer": "B",
        "explanation": "Los Santos is the main city in GTA V."
    },
    {
        "game": "Minecraft",
        "difficulty": "Medium",
        "question": "Which pickaxe can mine obsidian and drop it as a block?",
        "options": [
            "A. Wooden pickaxe",
            "B. Stone pickaxe",
            "C. Iron pickaxe",
            "D. Diamond pickaxe"
        ],
        "answer": "D",
        "explanation": "A diamond or netherite pickaxe can successfully mine obsidian."
    },
    {
        "game": "Fortnite",
        "difficulty": "Medium",
        "question": "What happens to the safe area during a standard "
                    "Battle Royale match?",
        "options": [
            "A. It gradually shrinks",
            "B. It covers the whole map forever",
            "C. It disappears before the match starts",
            "D. It only moves when a player wins"
        ],
        "answer": "A",
        "explanation": "The storm closes in, reducing the safe area."
    },
    {
        "game": "EA Sports FC",
        "difficulty": "Medium",
        "question": "Which game mode is focused on building a squad "
                    "using player items?",
        "options": [
            "A. Career Mode",
            "B. Ultimate Team",
            "C. Kick Off",
            "D. Practice Arena"
        ],
        "answer": "B",
        "explanation": "Ultimate Team lets you build and manage your squad."
    },
    {
        "game": "GTA V",
        "difficulty": "Medium",
        "question": "How many main playable protagonists are there "
                    "in GTA V's story mode?",
        "options": [
            "A. One",
            "B. Two",
            "C. Three",
            "D. Four"
        ],
        "answer": "C",
        "explanation": "The three protagonists are Michael, Franklin and Trevor."
    },
    {
        "game": "Minecraft",
        "difficulty": "Hard",
        "question": "Which hostile mob is famous for detecting "
                    "vibrations and reacting to nearby sounds?",
        "options": [
            "A. Warden",
            "B. Blaze",
            "C. Phantom",
            "D. Guardian"
        ],
        "answer": "A",
        "explanation": "The Warden uses vibration and smell detection "
                       "to locate nearby entities."
    },
    {
        "game": "GTA V / GTA Online",
        "difficulty": "Hard",
        "question": "Which GTA V protagonist is known for his "
                    "special ability to slow down time while driving?",
        "options": [
            "A. Michael",
            "B. Franklin",
            "C. Trevor",
            "D. Lamar"
        ],
        "answer": "B",
        "explanation": "Franklin's special ability slows time while driving."
    }
]

score = 0
total = len(questions)

# Ask each question
for number, q in enumerate(questions, start=1):
    print("\n" + "-" * 45)
    print(f"Question {number}/{total}")
    print(f"Game: {q['game']} | Difficulty: {q['difficulty']}")
    print(q["question"])

    for option in q["options"]:
        print(option)

    # Check that the player enters a valid choice
    while True:
        answer = input("\nYour answer (A/B/C/D): ").strip().upper()

        if answer in ("A", "B", "C", "D"):
            break

        print("Invalid choice! Please enter A, B, C or D.")

    # Check the answer
    if answer == q["answer"]:
        print("Correct! +1 point")
        score += 1
    else:
        print(f"Not quite! The correct answer is {q['answer']}.")

    print(q["explanation"])

# Final results
percentage = (score / total) * 100

print("\n" + "=" * 45)
print("             QUIZ COMPLETE!")
print("=" * 45)
print(f"Your score: {score}/{total}")
print(f"Percentage: {percentage:.0f}%")

if score == total:
    print("PERFECT SCORE! You are a gaming legend!")
elif score >= 8:
    print("Amazing! You really know your games!")
elif score >= 6:
    print("Great job! You know your gaming stuff.")
elif score >= 4:
    print("Not bad! Keep practising, gamer.")
else:
    print("Time for some more gaming practice!")

print("=" * 45)
print("Thanks for playing!")