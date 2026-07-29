
def main():
    number = int(input("Enter the number to print up to: "))
    for val in range(1,number+1):
        if val % 15 == 0:
            print("FizzBuzz")
        elif val % 5 == 0:
            print("Buzz")
        elif val % 3 == 0:
            print("Fizz")
        else:
            print(val)


if __name__ == "__main__":
    main()