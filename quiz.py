import csv
import random

def get_category():
    while True:
        categories = ["math", "solar system", "sports", "games", "random"]

        for c in categories:
            print("> "+c)

        choice = input("enter a category: ").lower()

        if choice not in categories:
            continue
        elif choice == "solar system":
            return choice.replace(" ", "").strip()
        else:
            return choice


def load_questions(filename):
    questions = []
    with open(f"{filename}.csv", mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            questions.append(row)
    return questions

def load_random():
    questions = []
    files = ["games.csv", "math.csv", "solarsystem.csv", "sports.csv"]

    for f in files:
        question_number = random.randint(1,4)
        with open(f,"r") as csvfile:
            read_questions = list(csv.DictReader(csvfile))
            while question_number > 0:
                to_be_appended = read_questions[random.randint(0, 9)]

                if to_be_appended not in questions:
                    questions.append(to_be_appended)
                    question_number -= 1
                else:
                    continue
    return questions


def run_quiz(questions):
    score = 0
    random.shuffle(questions)

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

    if category == "random":
        questions = load_random()
        run_quiz(questions)
    else:
        questions = load_questions(category)
        run_quiz(questions)
