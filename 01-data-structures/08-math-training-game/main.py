import time
import random
from datetime import datetime

def main():

    while True:
        try:
            mode = int(input("""What do you want to do?
            1. Play game
            2. See growth
            3. Quit
            Enter your choice: 
            """))
        except ValueError:
            print("Invalid input.")
            continue

        if mode == 1:
            play_game()
        elif mode == 2:
            load_record()
        elif mode == 3:
            break
        else:
            print("Invalid input.")


def play_game():
    score = 0
    total = 0
    start_time = time.time()
    while time.time() - start_time < 120:
        total += 1
        op = random.choice(["+", "-", "*", "/"])
        if op == "+" or op == "-":
            first_int = random.randint(2, 102)
            second_int = random.randint(2, 102)
            sum = first_int + second_int
            if op == "+":
                try:
                    res = int(input(f"{first_int} + {second_int} = "))
                    if res == sum:
                        score += 1
                except ValueError:
                    continue
            else:
                try:
                    res = int(input(f"{sum} - {first_int} = "))
                    if res == second_int:
                        score += 1
                except ValueError:
                    continue

        else:
            first_int = random.randint(2, 12)
            second_int = random.randint(2, 100)
            product = first_int * second_int
            if op == "*":
                try:
                    res = int(input(f"{first_int} * {second_int} = "))
                    if res == product:
                        score += 1
                except ValueError:
                    continue
            else:
                try:
                    res = int(input(f"{product} / {first_int} = "))
                    if res == second_int:
                        score += 1
                except ValueError:
                    continue
    print(f"\nYou had {score} correct answers out of {total} questions.\n")
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    with open("record.txt", "a", encoding="utf-8") as file:
        file.write(f"{stamp} -> {score} correct answers out of {total} attempts.\n")

def load_record():
    try:
        with open("record.txt","r", encoding="utf-8") as f:
            lines = f.readlines()
            print()
            for line in lines[-20:]:
                print(line.strip())
            print()
    except FileNotFoundError:
        print("No records yet.")


if __name__ == "__main__":
    main()