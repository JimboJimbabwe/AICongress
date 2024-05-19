import os
import re
import random
import argparse

def read_or_create_default_values(file_path):
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            file.write("temperature=0.01\nmax_tokens=2000\n")
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def scan_and_edit_congress_files(congress_paths_file, default_values, mode):
    with open(congress_paths_file, 'r') as file:
        congress_files = [line.strip() for line in file.readlines()]

    for file_path in congress_files:
        if not file_path.endswith('.py'):
            continue

        with open(file_path, 'r') as file:
            lines = file.readlines()

        edited = False
        for i, line in enumerate(lines):
            for default_value in default_values:
                if default_value in line:
                    if mode == "autoassign":
                        if "temperature=" in default_value:
                            new_value = str(round(random.uniform(0.01, 3.00), 2))
                            print(f"Automatically assigned temperature: {new_value} in {file_path}")
                        elif "max_tokens=" in default_value:
                            new_value = str(random.randint(200, 80000))
                            print(f"Automatically assigned max_tokens: {new_value} in {file_path}")
                        else:
                            new_value = "random_value"  # Replace with appropriate random logic if needed
                            print(f"Automatically assigned value: {new_value} in {file_path}")
                    elif mode == "default":
                        new_value = default_value.split('=')[1]
                        print(f"Assigned default value: {new_value} in {file_path}")
                    else:
                        print(f"Current line in {file_path}: {line.strip()}")
                        if "temperature=" in default_value:
                            new_value = input("Enter a float between 0.01 and 3.00 (or press 'r' for random): ")
                            if new_value.lower() == 'r':
                                new_value = str(round(random.uniform(0.01, 3.00), 2))
                                print(f"Randomly assigned temperature: {new_value}")
                        elif "max_tokens=" in default_value:
                            new_value = input("Enter an integer between 200 and 80000 (or press 'r' for random): ")
                            if new_value.lower() == 'r':
                                new_value = str(random.randint(200, 80000))
                                print(f"Randomly assigned max_tokens: {new_value}")
                        else:
                            new_value = input("Enter new value: ")
                            if new_value.lower() == 'r':
                                new_value = "random_value"  # Replace with appropriate random logic if needed
                                print(f"Randomly assigned value: {new_value}")
                    lines[i] = re.sub(r'(?<==).*', new_value, line)
                    edited = True

        if edited:
            with open(file_path, 'w') as file:
                file.writelines(lines)

def main():
    parser = argparse.ArgumentParser(description="Edit or auto-assign random/default values to Python files.")
    parser.add_argument('-autoassign', action='store_true', help="Automatically assign random values")
    parser.add_argument('-default', action='store_true', help="Automatically assign default values")
    args = parser.parse_args()

    default_values_path = "Source/DefaultValues.txt"
    default_values = read_or_create_default_values(default_values_path)

    mode = None
    if args.autoassign:
        mode = "autoassign"
    elif args.default:
        mode = "default"

    if mode is None:
        edit = input("Would you like to edit the values? (Y/N): ")
        if edit.lower() != 'y':
            print("No changes made. Exiting.")
            return

    session_number = input("Enter the session number (N): ")
    congress_paths_file = f"Congress/Session{session_number}/congressPaths.txt"

    if not os.path.exists(congress_paths_file):
        print(f"The file {congress_paths_file} does not exist. Exiting.")
        return

    scan_and_edit_congress_files(congress_paths_file, default_values, mode)
    print("Editing completed.")

if __name__ == "__main__":
    main()

