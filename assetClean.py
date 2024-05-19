import os
import shutil

def restore_and_clean_backup():
    # Get the current working directory
    current_dir = os.getcwd()
    # Define the backup directory path
    backup_dir = os.path.join(current_dir, "Source", "Backups")

    # Ensure the backup directory exists
    if not os.path.exists(backup_dir):
        print(f"Backup directory {backup_dir} does not exist.")
        return

    # Loop through all files in the backup directory
    for filename in os.listdir(backup_dir):
        # Check if the file is a .py file and is not "main.py"
        if filename.endswith(".py") and filename != "main.py":
            # Create the full path to the backup file
            backup_file = os.path.join(backup_dir, filename)
            # Create the full path to the destination file in the current directory
            destination_file = os.path.join(current_dir, filename)
            # Copy the file to the current directory, overwriting if it exists
            shutil.copy2(backup_file, destination_file)
            print(f"Copied: {backup_file} to {destination_file}")

    # Delete all files in the backup directory
    for filename in os.listdir(backup_dir):
        file_path = os.path.join(backup_dir, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)  # Remove the file or link
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)  # Remove the directory and its contents
            print(f"Deleted: {file_path}")
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")

# Run the restore and clean function
restore_and_clean_backup()

