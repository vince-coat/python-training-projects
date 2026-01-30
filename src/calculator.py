# Create a command-line calculator that asks the user to enter
# two numbers and then displays the result of adding those two numbers.

def addition(first_number: float, second_number: float) -> float:
    """Returns the sum of two numbers."""
    return first_number + second_number


def get_number(prompt):
    """Prompts the user for a number and returns it as a float."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# ask the user for two numbers
first_number = get_number("Enter the first number: ")
second_number = get_number("Enter the second number: ")

# calculate and display the sum
result = addition(first_number, second_number)
print(f"The sum of {first_number} and {second_number} is {result}.")
