def collatz_sequence(number):
    while number != 1:
        print(number, end=" ")
        if number % 2 == 0:  # If the number is even
            number //= 2
        else:  # If the number is odd
            number = number * 3 + 1
    print(number)  # Print the final number (1)

if __name__ == "__main__":
    try:
        user_input = int(input("Please enter a positive integer: "))
        if user_input <= 0:
            print("The number must be a positive integer.")
        else:
            collatz_sequence(user_input)
    except ValueError:
        print("Invalid input. Please enter a positive integer.")