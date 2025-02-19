import csv

def get_category():
    while True:
        categories = ["math", "solar system", "sports", "games"]

        for c in categories:
            print("> "+c)

        choice = input("enter a category: ").lower()

        if choice not in categories:
            continue
        else:

            return choice.replace(" ", "").strip()


def load_questions(filename):
    questions = []
    with open(f"{filename}.csv", mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            questions.append(row)
    return questions

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question['Question'])
        print(f"A: {question['Option A']}")
        print(f"B: {question['Option B']}")
        print(f"C: {question['Option C']}")
        print(f"D: {question['Option D']}")
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer == question['Correct Answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {question['Correct Answer']}.\n")
    print(f"Quiz finished! Your score is {score}/{len(questions)}.")

if __name__ == "__main__":

    category = get_category()
    questions = load_questions(category)
    run_quiz(questions)
