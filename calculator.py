def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def get_numbers():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input. Please enter numeric values.")

def main():
    print("Simple Calculator")
    print("=================")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Quit")

    while True:
        choice = input("Enter choice (1/2/3/4/5): ")

        if choice in ('1', '2', '3', '4'):
            num1, num2 = get_numbers()

            if choice == '1':
                print(f"The result of {num1} + {num2} is {add(num1, num2)}")
            elif choice == '2':
                print(f"The result of {num1} - {num2} is {subtract(num1, num2)}")
            elif choice == '3':
                print(f"The result of {num1} * {num2} is {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"The result of {num1} / {num2} is {result}")

        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
