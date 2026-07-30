import time
import random

def main():
    while True:
        try:
            number_questions = int(input("How many questions do you want to solve? -> "))
        except ValueError:
            print("That's not a number.")
            return

        try:
            max_int = int(input("What's the maximum number of which you want to drill its multiplication table? -> "))
        except ValueError:
            print("That's not a number.")
            return
        start_time = time.time()
        correct_answers = 0

        for question in range(number_questions):
            val_one = random.randint(1, max_int)
            val_two = random.randint(1, max_int)

            solution = val_one * val_two

            try:
                response = int(input(f"Answer: {val_one} x {val_two} --> "))

            except ValueError:
                print("That's not a number.")
                return

            if response == solution:
                correct_answers += 1

        end_time = time.time()

        total_time = round((end_time - start_time),2)
        avg_time = total_time / number_questions

        print(f"""
        - Total score: {correct_answers}/{number_questions} 
        - Total time: {total_time} s
        - Average time per question: {round(avg_time, 2)} s
    """)
        play_again = input("Do you want to play again? (y/n) -> ")
        if play_again != "y":
            break



if __name__ == "__main__":
    main()