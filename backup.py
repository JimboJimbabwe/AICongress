import os
import shutil

def backup_python_files():
    # Get the current working directory
    current_dir = os.getcwd()
    # Define the backup directory path
    backup_dir = os.path.join(current_dir, "Source", "Backups")

    # Ensure the backup directory exists
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    # Loop through all files in the current directory
    for filename in os.listdir(current_dir):
        # Check if the file is a .py file
        if filename.endswith(".py"):
            # Create the full path to the source file
            source_file = os.path.join(current_dir, filename)
            # Create the full path to the backup file
            backup_file = os.path.join(backup_dir, filename)
            # Copy the file to the backup directory
            shutil.copy2(source_file, backup_file)
            print(f"Copied: {source_file} to {backup_file}")

# Run the backup function
backup_python_files()

