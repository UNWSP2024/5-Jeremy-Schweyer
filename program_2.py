# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as

import random
def math_quiz_sum():
    numbers1 = list(range(1, 300))
    random1 = random.choice(numbers1)
    random2 = random.choice(numbers1)

    return random1, random2
if __name__ == '__main__':
    random1, random2 = math_quiz_sum()
    sum1 = random1 + random2
    print("Your equation is:",random1,"+", random2)
    answer = int(input("What is the answer to the equation?:"))
    if answer == sum1:
        print("Congratulations you got it right")
    else:
        print("Incorrect, the correct answer is", sum1)
