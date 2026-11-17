# Python Toolkit

This beginner-friendly, menu-driven toolkit contains a number guessing game, a to-do list, and a simple calculator. The game practices loops and conditionals, the to-do list changes as you add or remove tasks, and the calculator handles four basic operations.

## How to run

Open a terminal in this repository and run:

```text
python toolkit.py
```

Choose a numbered option at the main menu. The to-do list keeps its tasks until the program exits, and you can return to the main menu from each tool.

## Screenshots

The `screenshots/` folder is reserved for the invalid-menu-choice example and one screenshot of each tool in action. These captures still need to be added.

## Reflection

The hardest part was making the to-do list keep its changes while still returning cleanly to the main menu. The bug that took the longest to fix was handling invalid input without leaving a tool or crashing the program. Testing empty tasks, incorrect task numbers, and division by zero helped make the menus more reliable. I learned how loops, conditionals, and lists can work together in a small interactive program. I also learned to check user input before using it in calculations or list operations. With one more week, I would save the to-do list to a file so tasks remain available after the program closes.