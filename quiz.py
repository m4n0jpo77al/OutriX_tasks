import json
import random

# Load questions from JSON file
def load_questions(filename='questions.json'):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Questions file not found!")
        return []

# Run the quiz
def run_quiz(questions):
    score = 0
    random.shuffle(questions)  # Shuffle question order

    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q['question']}")
        options = q['options']
        random.shuffle(options)  # Shuffle options
        for idx, option in enumerate(options, 1):
            print(f"  {idx}. {option}")
        
        try:
            choice = int(input("Your answer (1-4): "))
            if options[choice - 1] == q['answer']:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong! Correct answer: {q['answer']}")
        except (ValueError, IndexError):
            print(f"⚠️ Invalid input. Correct answer: {q['answer']}")

    print("\n--- QUIZ COMPLETE ---")
    print(f"Your final score: {score}/{len(questions)}")

# Main
if __name__ == "__main__":
    print("Welcome to the Quiz App!")
    questions = load_questions()
    if questions:
        run_quiz(questions)
