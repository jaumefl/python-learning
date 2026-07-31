def main():
    conversions = {
        1: (celsius_to_fahrenheit, "degrees Celsius", "degrees Fahrenheit"),
        2: (fahrenheit_to_celsius, "degrees Fahrenheit", "degrees Celsius"),
        3: (kilometres_to_miles, "kilometres", "miles"),
        4: (miles_to_kilometres, "miles", "kilometres"),
        5: (kilograms_to_pounds, "kilograms", "pounds"),
        6: (pounds_to_kilograms, "pounds", "kilograms"),
    }

    while True:

        try:
            choice = int(input("""Select what conversion you want to perform:
            1. Celsius -> Fahrenheit
            2. Fahrenheit -> Celsius
            3. Kilometres -> Miles
            4. Miles -> Kilometres
            5. Kilograms -> Pounds
            6. Pounds - Kilograms
            7. Quit
            Select a number --> """))
        except ValueError:
            print("That's not a number.")
            continue

        if choice == 7:
            break
        if choice not in conversions:
            print("That's not a valid choice.")
            continue

        func, label, res = conversions[choice]

        try:
            value = float(input(f"Enter {label}: "))
        except ValueError:
            print("That's not a number.")
            continue

        converted = round(func(value),2)
        print(f"Its conversion is {converted} {res}")

def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def kilometres_to_miles(kilometres):
    return kilometres * 0.62137

def miles_to_kilometres(miles):
    return miles * 1.60934

def kilograms_to_pounds(kilograms):
    return kilograms * 2.20462

def pounds_to_kilograms(pounds):
    return pounds * 0.453591

if __name__ == "__main__":
    main()