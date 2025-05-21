import os

def clean_solution(file_path):

    """
    Cleans the implementation code from a LeetCode-style solution file.

    Removes lines between the method definition (def ...)
    and the start of the docstring.

    Args:
        file_path (str): The path to the Python file to clean.
    """

    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return

    print(f"Attempting to clear solution code from {file_path}...")

    # Read the file
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        class_Solution_index = -1
        comment_testing_index = -1
        no_solution_lines = []

        for n, i in enumerate(lines):
            if "class Solution" in i:
                class_Solution_index = n + 2 # For the extra two lines
            if '// Testing' in i:
                comment_testing_index = n - 2
            if class_Solution_index > 0 and comment_testing_index > 0:
                no_solution_lines = lines[:class_Solution_index+1] + ['\n\n'] + lines[comment_testing_index:]
                break

        # Write the cleaned content back to the file
        if no_solution_lines != []:
            with open(file_path, 'w') as file:
                file.writelines(no_solution_lines)
                print(f"{file_path} is now clean, appears to be success.")
        else:
            print(f"No lines found in {file_path}")

    except Exception as e:
        print(f"An error occurred during file cleaning: {e}")
