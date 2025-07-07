import os
from typing_extensions import overload

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

        def_index = -1
        q_index = -1
        no_solution_lines = []

        for n, i in enumerate(lines):
            if "def" in i:
                def_index = n
            if i == '"""\n':
                q_index = n
            elif def_index > 0 and q_index > 0:
                no_solution_lines = lines[:def_index+1] + ['\t\tpass\n\n'] + lines[q_index:]
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


dir_ = "0_arrays/"
# [clean_solution(f"{dir_}/{file}") for file in os.listdir(dir_) if "py" in file]
