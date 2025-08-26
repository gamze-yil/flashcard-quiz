# flashcard_quiz.py

# German to English flashcards
flashcards = {
    "Hund": "dog",
    "Katze": "cat",
    "Haus": "house",
    "Wasser": "water",
    "Buch": "book"
}
# flashcard_quiz.py (continued)

print("🧠 German-English Flashcard Quiz 🧠")
print("Type the English meaning of each German word.\n")

score = 0  # Track correct answers

for german, english in flashcards.items():
    answer = input(f"What does '{german}' mean in English? ").strip().lower()

    if answer == english.lower():
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Oops! The correct answer is '{english}'.\n")

print(f"🎉 You got {score}/{len(flashcards)} correct. Gut gemacht!")
