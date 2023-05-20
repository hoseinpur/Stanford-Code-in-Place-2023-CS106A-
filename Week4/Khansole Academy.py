import random

def generate_problem():
    num1 = random.randint(10, 99)
    num2 = random.randint(10, 99)
    return num1, num2

def get_user_answer():
    try:
        answer = int(input("Your answer: "))
        return answer
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return get_user_answer()

def check_answer(num1, num2, answer):
    expected = num1 + num2
    if answer == expected:
        return True
    else:
        print(f"Incorrect. The expected answer is {expected}.")
        return False

def khansole_academy():
    correct_count = 0
    consecutive_correct = 0

    print("Khansole Academy")

    while consecutive_correct < 3:
        num1, num2 = generate_problem()
        print(f"What is {num1} + {num2}?")
        user_answer = get_user_answer()

        if check_answer(num1, num2, user_answer):
            correct_count += 1
            consecutive_correct += 1
            print(f"Correct! You've gotten {consecutive_correct} correct in a row.")
        else:
            consecutive_correct = 0

    print("Congratulations! You mastered addition.")

khansole_academy()
