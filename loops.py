def main():
    print("Hello! Here are the numbers from 1 to 10:")

    for i in range(1, 11):
        print(i)
    user_input = input("Enter a number between 1 and 10: ")

    try:
        number = int(user_input)
        if 1 <= number <= 10:
            print(f"You entered {number}, which is within the range!")
        else:
            print(f"{number} is out of range. Please enter a number between 1 and 10.")
    except ValueError:
        print(f"{user_input} is not a valid number. Please enter a valid integer")

    print("Goodbye!")

if __name__ == "__main__":
    main()
