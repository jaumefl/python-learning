def main():
    try:
        first_operand = float(input("Enter first operand: "))
    except ValueError:
        print("That's not a number.")
        return
    try:
        second_operand = float(input("Enter second operand: "))
    except ValueError:
        print("That's not a number.")
        return
    operator = input(
    """Select one of the following operators: 
 1. Sum +
 2. Subtract - 
 3. Multiply * 
 4. Divide (float) / 
 5. Power ^ 
 6. Modulo %
 Enter the operator number: """)
    if operator == "1":
        res = sum(first_operand, second_operand)
    elif operator == "2":
        res = subtract(first_operand, second_operand)
    elif operator == "3":
        res = multiply(first_operand, second_operand)
    elif operator == "4":
        res = divide(first_operand, second_operand)
    elif operator == "5":
        res = power(first_operand, second_operand)
    elif operator == "6":
        res = modulo(first_operand, second_operand)

    else:
        print("Select one of the available operators")
        return

    print("Result: ", res)




def add(first_operand, second_operand):
    return first_operand + second_operand

def subtract(first_operand, second_operand):
    return first_operand - second_operand

def multiply(first_operand, second_operand):
    return first_operand * second_operand

def divide(first_operand, second_operand):
    if second_operand == 0:
        print("Can't divide by zero.")
        return None
    return first_operand / second_operand

def power(first_operand, second_operand):
    return first_operand ** second_operand

def modulo(first_operand, second_operand):
    return first_operand % second_operand

if __name__ == "__main__":
    main()