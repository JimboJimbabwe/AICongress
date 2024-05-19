import os

def get_available_sessions():
    sessions = [folder for folder in os.listdir("Congress") if folder.startswith("Session")]
    return sessions

def enumerate_folders(session_folder):
    folders = [folder for folder in os.listdir(os.path.join("Congress", session_folder)) if os.path.isdir(os.path.join("Congress", session_folder, folder))]
    return folders

def enumerate_folder_contents(session_folder, folder):
    contents = os.listdir(os.path.join("Congress", session_folder, folder))
    return contents

def get_python_script_path(session_folder, folder):
    for file in os.listdir(os.path.join("Congress", session_folder, folder)):
        if file.endswith(".py"):
            return os.path.join("Congress", session_folder, folder, file)
    return None

def save_paths_to_file(session_folder, paths):
    file_path = os.path.join("Congress", session_folder, "congressPaths.txt")
    with open(file_path, "w") as file:
        file.write("\n".join(paths))

def update_scripts_with_session(session_number):
    for script in ["collector.py", "cleaner.py"]:
        with open(script, "r") as file:
            content = file.read()
        
        updated_content = content.replace("[S]", str(session_number))
        
        with open(script, "w") as file:
            file.write(updated_content)

def process_sessions():
    sessions = get_available_sessions()
    if not sessions:
        print("No available sessions found.")
        return

    print("Available sessions:")
    for index, session in enumerate(sessions, start=1):
        print(f"{index}. {session}")

    choice = int(input("Enter the number of the session you want to choose: "))
    selected_session = sessions[choice - 1]
    session_number = selected_session.replace("Session", "")

    folders = enumerate_folders(selected_session)
    print(f"\nFolders in {selected_session}:")
    for folder in folders:
        print(folder)

    print(f"\nContents of folders in {selected_session}:")
    for folder in folders:
        contents = enumerate_folder_contents(selected_session, folder)
        print(f"{folder}:")
        for item in contents:
            print(f"  {item}")

    print(f"\nPython script paths in {selected_session}:")
    paths = []
    for folder in folders:
        script_path = get_python_script_path(selected_session, folder)
        if script_path:
            paths.append(script_path)
            print(script_path)

    save_paths_to_file(selected_session, paths)
    print(f"\nPython script paths saved to {selected_session}/congressPaths.txt")

    # Update collector.py and cleaner.py with the session number
    update_scripts_with_session(session_number)

# Run the script
process_sessions()

