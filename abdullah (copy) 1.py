def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return "Error, division by 0 is not possible"
    return x / y

def main():
    while True:
        print("\nSimple Calculator")
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        # Taking input from the user
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))

            if choice == '1':
                print(f"The result is: {addition(num1, num2)}")
            elif choice == '2':
                print(f"The result is: {subtraction(num1, num2)}")
            elif choice == '3':
                print(f"The result is: {multiplication(num1, num2)}")
            elif choice == '4':
                print(f"The result is: {division(num1, num2)}")
        else:
            print("Invalid input. Please enter a number between 1 and 5")

if __name__ == "__main__":
    main()
