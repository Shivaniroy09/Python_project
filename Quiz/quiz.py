import os

# Function to load questions from a file
def load_questions(filename):
    questions = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            question = parts[0]
            options = parts[1:5]
            correct_answer = parts[5]
            questions.append((question, options, correct_answer))
    return questions

# Function to display the quiz and get the user's score
def conduct_quiz(questions):
    score = 0
    for index, (question, options, correct_answer) in enumerate(questions):
        print(f"Question {index + 1}: {question}")
        for i, option in enumerate(options):
            print(f"{chr(65 + i)}. {option}")  # A, B, C, D
        answer = input("Your Answer: ").strip().upper()

        if answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {correct_answer}.\n")
    
    return score

# Function to save the user's score to a file
def save_score(username, score, total_questions):
    with open('scores.txt', 'a') as file:
        file.write(f"{username},{score}/{total_questions}\n")
    print(f"Score recorded in scores.txt")

# Main function to run the quiz application
def main():
    print("Welcome to the Quiz Application!")
    print("Rules:")
    print("- Each question has 4 options.")
    print("- Enter the option (A, B, C, D) as your answer.")
    input("Press Enter to Start!")

    questions = load_questions('questions.txt')
    username = input("Enter your name: ")
    score = conduct_quiz(questions)

    print(f"Quiz Complete!")
    print(f"Your Score: {score}/{len(questions)}")
    save_score(username, score, len(questions))

if __name__ == "__main__":
    main()
    