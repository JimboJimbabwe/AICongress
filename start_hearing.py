import os

def create_vault_files(paths):
    for path in paths:
        folder = os.path.dirname(path)
        vault_file = os.path.join(folder, "vault.txt")
        if not os.path.exists(vault_file):
            with open(vault_file, "w") as file:
                file.write("")
            print(f"Created {vault_file}")
        else:
            print(f"File {vault_file} already exists. Skipping creation.")

def replace_placeholder(file_path, placeholder, replacement):
    with open(file_path, "r") as file:
        content = file.read()
    updated_content = content.replace(placeholder, replacement)
    with open(file_path, "w") as file:
        file.write(updated_content)

def update_congress_member_scripts(paths, placeholder, name_placeholder):
    placeholders_found = False
    for path in paths:
        with open(path, "r") as file:
            content = file.read()
            if placeholder in content:
                placeholders_found = True
                break

    if placeholders_found:
        user_input = input("Enter the replacement string for <PLACEHOLDER>: ")
        for path in paths:
            folder_name = os.path.basename(os.path.dirname(path))
            replace_placeholder(path, placeholder, user_input)
            replace_placeholder(path, name_placeholder, folder_name)
            print(f"Placeholders replaced in {path}")
    else:
        print("No placeholders found in the scripts. Skipping replacement process.")

def update_integer_value(paths, search_string):
    integer_found = False
    for path in paths:
        with open(path, "r") as file:
            content = file.read()
            if search_string in content:
                integer_found = True
                break

    if integer_found:
        while True:
            user_input = input("Enter an integer value to replace [A]: ")
            if user_input.isdigit():
                break
            else:
                print("Invalid input. Please enter an integer value.")

        for path in paths:
            with open(path, "r") as file:
                content = file.read()
            updated_content = content.replace(search_string, user_input)
            with open(path, "w") as file:
                file.write(updated_content)
            print(f"Integer value updated in {path}")
    else:
        print("No integer placeholders found in the scripts. Skipping update process.")

def run_congress_member_scripts(paths):
    for path in paths:
        os.system(f"python {path}")

def get_available_sessions():
    sessions = [folder for folder in os.listdir("Congress") if folder.startswith("Session")]
    return sessions

def process_congress_paths(session_folder):
    file_path = os.path.join("Congress", session_folder, "congressPaths.txt")
    if not os.path.exists(file_path):
        print(f"{file_path} not found.")
        return
    with open(file_path, "r") as file:
        paths = file.read().splitlines()
    create_vault_files(paths)
    placeholder = "<PLACEHOLDER>"
    name_placeholder = "<NAME>"
    update_congress_member_scripts(paths, placeholder, name_placeholder)
    
    search_string = "[A]"
    update_integer_value(paths, search_string)
    
    run_congress_member_scripts(paths)

# Get available session folders
sessions = get_available_sessions()
if not sessions:
    print("No session folders found.")
else:
    print("Available session folders:")
    for index, session in enumerate(sessions, start=1):
        print(f"{index}. {session}")
    
    while True:
        choice = input("Enter the number of the session folder to process (or 'q' to quit): ")
        if choice == 'q':
            break
        try:
            choice = int(choice)
            if 1 <= choice <= len(sessions):
                selected_session = sessions[choice - 1]
                process_congress_paths(selected_session)
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid choice. Please enter a valid number.")
