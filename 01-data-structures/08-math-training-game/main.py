import time
import random
import csv
from pathlib import Path
from datetime import datetime

RESULTS = Path(__file__).parent / "results.csv"

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
    save_result(score, total)


def save_result(score, total):
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    new_file = not RESULTS.exists()
    with open(RESULTS, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if new_file:
            writer.writerow(["timestamp", "correct", "total"])
        writer.writerow([stamp, score, total])

def load_record():
    try:
        with open(RESULTS, "r", newline="", encoding="utf-8") as f:
            rows = list(csv.reader(f))
    except FileNotFoundError:
        print("No records yet.")
        return

    print()
    for stamp, correct, total in rows[1:][-20:]:
        print(f"{stamp} -> {correct}/{total}")
    print()

if __name__ == "__main__":
    main()