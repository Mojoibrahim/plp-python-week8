"""A small menu-driven toolkit for practicing Python fundamentals."""

import random


def number_guessing_game():
    """Run a number guessing game and report hints until the answer is found."""
    answer = random.randint(1, 10)
    guesses = 0

    print("\nI'm thinking of a number from 1 to 10.")
    while True:
        guess_text = input("Your guess (or 'q' to return to the menu): ").strip()
        if guess_text.lower() == "q":
            print("No problem! Returning to the main menu.")
            return

        try:
            guess = int(guess_text)
        except ValueError:
            print("Please enter a whole number from 1 to 10, or 'q' to quit.")
            continue

        if not 1 <= guess <= 10:
            print("That number is outside the range. Please choose 1 to 10.")
            continue

        guesses += 1
        if guess < answer:
            print("Too low - try a higher number.")
        elif guess > answer:
            print("Too high - try a lower number.")
        else:
            print(f"You got it! The number was {answer}. Guesses: {guesses}.")
            return


def todo_list(tasks):
    """Let the user view, add, and remove tasks in a shared list."""
    while True:
        print("\n--- To-Do List ---")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Back to the main menu")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            if not tasks:
                print("Your to-do list is empty.")
            else:
                print("Your tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")
        elif choice == "2":
            task = input("What would you like to add? ").strip()
            if task:
                tasks.append(task)
                print(f"Added: {task}")
            else:
                print("A task can't be empty, so nothing was added.")
        elif choice == "3":
            if not tasks:
                print("There are no tasks to remove.")
                continue

            try:
                task_number = int(input("Enter the task number to remove: ").strip())
            except ValueError:
                print("Please enter a valid task number.")
                continue

            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"Removed: {removed_task}")
            else:
                print(f"Please choose a task number from 1 to {len(tasks)}.")
        elif choice == "4":
            return
        else:
            print("That option isn't on the to-do menu. Please choose 1 to 4.")


def simple_calculator():
    """Calculate a basic arithmetic operation using two numbers."""
    print("\n--- Simple Calculator ---")
    try:
        first_number = float(input("Enter the first number: ").strip())
        operator = input("Choose an operation (+, -, *, /): ").strip()
        second_number = float(input("Enter the second number: ").strip())
    except ValueError:
        print("Please enter valid numbers. Returning to the main menu.")
        return

    if operator == "+":
        result = first_number + second_number
    elif operator == "-":
        result = first_number - second_number
    elif operator == "*":
        result = first_number * second_number
    elif operator == "/":
        if second_number == 0:
            print("Division by zero isn't allowed.")
            return
        result = first_number / second_number
    else:
        print("That operation isn't supported. Please use +, -, *, or /.")
        return

    print(f"{first_number:g} {operator} {second_number:g} = {result:g}")


def main():
    """Show the toolkit menu until the user chooses to quit."""
    tasks = []
    print("Welcome to the Python Toolkit!")

    while True:
        print("\n=== PYTHON TOOLKIT ===")
        print("1. Number Guessing Game")
        print("2. To-Do List")
        print("3. Simple Calculator")
        print("4. Quit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            number_guessing_game()
        elif choice == "2":
            todo_list(tasks)
        elif choice == "3":
            simple_calculator()
        elif choice == "4":
            print("Thanks for using the Python Toolkit. Have a great day!")
            break
        else:
            print("Sorry, that choice isn't on the menu. Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()