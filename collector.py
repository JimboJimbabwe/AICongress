import os
import shutil

# Placeholder Session1 for session number
session_number = "1"

def create_response_repo():
    if not os.path.exists("responseRepo"):
        os.makedirs("responseRepo")

def collect_responses():
    response_folder = "response"
    response_files = [file for file in os.listdir(response_folder) if file.endswith(".txt")]
    
    vault_file = os.path.join("responseRepo", "vault.txt")
    
    with open(vault_file, "w") as vault:
        for file in response_files:
            file_path = os.path.join(response_folder, file)
            with open(file_path, "r") as response:
                content = response.read()
                vault.write(content + "\n")
    
    return vault_file

def distribute_vault(vault_file, congress_paths_file):
    with open(congress_paths_file, "r") as paths_file:
        paths = paths_file.read().splitlines()
    
    for path in paths:
        folder_path = os.path.dirname(path)
        vault_dest = os.path.join(folder_path, "vault.txt")
        
        if os.path.exists(vault_dest):
            with open(vault_dest, "r") as existing_vault:
                existing_content = existing_vault.read()
            
            with open(vault_file, "r") as new_vault:
                new_content = new_vault.read()
            
            combined_content = existing_content + "\n" + new_content
            
            with open(vault_dest, "w") as combined_vault:
                combined_vault.write(combined_content)
        else:
            shutil.copy(vault_file, vault_dest)

def overwrite_session_vaults(vault_file, session_folder):
    for root, dirs, files in os.walk(session_folder):
        if "vault.txt" in files:
            vault_path = os.path.join(root, "vault.txt")
            shutil.copy(vault_file, vault_path)

def main():
    create_response_repo()
    vault_file = collect_responses()
    
    congress_paths_file = f"Congress/Session{session_number}/congressPaths.txt"
    distribute_vault(vault_file, congress_paths_file)
    
    session_folder = os.path.dirname(congress_paths_file)
    overwrite_session_vaults(vault_file, session_folder)

if __name__ == "__main__":
    main()

