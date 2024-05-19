import re

# Placeholder Session1 for session number
session_number = "1"

def update_stage_number(file_path):
    # Read the contents of the file
    with open(file_path, "r") as file:
        content = file.read()

    # Define the regular expression pattern to match the string
    pattern = r"This is currently stage (\d+) of the experiment."

    # Search for the pattern in the content
    match = re.search(pattern, content)

    if match:
        # Extract the current stage number
        current_stage = int(match.group(1))

        # Increment the stage number by 1
        new_stage = current_stage + 1

        # Replace the old stage number with the new one
        updated_content = re.sub(pattern, f"This is currently stage {new_stage} of the experiment.", content)

        # Write the updated content back to the file
        with open(file_path, "w") as file:
            file.write(updated_content)

        print(f"Stage number updated from {current_stage} to {new_stage} in {file_path}")
    else:
        print(f"No stage number found in {file_path}")

# Define the path to the congressPaths.txt file using the session number
congress_paths_file = f"Congress/Session{session_number}/congressPaths.txt"

# Read the congressPaths file and get the list of file paths
with open(congress_paths_file, "r") as wordlist_file:
    file_paths = wordlist_file.read().splitlines()

# Iterate over each file path in the congressPaths file and update the stage number
for file_path in file_paths:
    update_stage_number(file_path)

