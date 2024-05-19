import os
import random
import shutil

def create_congress_folder():
    if not os.path.exists("Congress"):
        os.makedirs("Congress")

def create_session_folder():
    session_number = 1
    while True:
        session_folder = f"Session{session_number}"
        if not os.path.exists(os.path.join("Congress", session_folder)):
            os.makedirs(os.path.join("Congress", session_folder))
            return session_folder
        session_number += 1

def generate_names(session_folder, num_names):
    first_names = ["John", "Emma", "Michael", "Sophia", "William", "Olivia", "James", "Ava", "Benjamin", "Isabella"]
    last_names = ["Smith", "Johnson", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor", "Anderson", "Thomas"]

    with open(os.path.join("Congress", session_folder, "names.txt"), "w") as file:
        for _ in range(num_names):
            first_name = random.choice(first_names)
            last_name = random.choice(last_names)
            file.write(f"{first_name} {last_name}\n")

def create_member_folders(session_folder):
    with open(os.path.join("Congress", session_folder, "names.txt"), "r") as file:
        names = file.readlines()

    for name in names:
        first_name, last_name = name.strip().split(" ")
        member_folder = f"{first_name}{last_name}Congress"
        member_folder_path = os.path.join("Congress", session_folder, member_folder)
        if not os.path.exists(member_folder_path):
            os.makedirs(member_folder_path)
            os.makedirs(os.path.join(member_folder_path, "responses"))
        else:
            print(f"Directory {member_folder_path} already exists. Skipping creation.")

        source_file = "Source/BaseFile.py"
        destination_file = os.path.join(member_folder_path, f"{last_name}CongressMember.py")
        shutil.copy(source_file, destination_file)

def create_session():
    create_congress_folder()

    while True:
        create_session_input = input("Do you want to create a new session? (y/n): ")
        if create_session_input.lower() == "y":
            session_folder = create_session_folder()
            num_names = int(input("Enter the number of names to generate: "))
            generate_names(session_folder, num_names)
            create_member_folders(session_folder)
            print(f"Session {session_folder} created successfully.")
        else:
            break

# Run the script
create_session()
