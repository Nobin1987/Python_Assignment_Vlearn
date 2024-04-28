# In DevOps, performing regular backups of important files is crucial:

# ●       Implement a Python script called backup.py that takes a source directory and a 
# destination directory as command-line arguments.

# ●       The script should copy all files from the source directory to the destination directory.

# ●       Before copying, check if the destination directory already contains a file with the same name. If so, append a 
# timestamp to the file name to ensure uniqueness.

# ●       Handle errors gracefully, such as when the source directory or destination directory does not exist.

# Sample Command:

# python backup.py /path/to/source /path/to/destination

# By running the script with the appropriate source and destination directories, 
# it should create backups of the files in the source directory, ensuring unique file names in the destination directory.

import os
import shutil
import sys
from datetime import datetime

def backup_files(S_DIR, D_DIR):
    # Check if source directory exists
    print("starting function")
    if not os.path.exists(S_DIR):
        print("Source directory does not exist.")
        return

    # Check if destination directory exists, create if not
    if not os.path.exists(D_DIR):
        os.makedirs(D_DIR)

    # Get list of files in source directory
    files = os.listdir(S_DIR)

    # Copy files to destination directory
    for file in files:
        source_path = os.path.join(S_DIR, file)
        dest_path = os.path.join(D_DIR, file)

        # If file with same name exists in destination, append timestamp
        if os.path.exists(dest_path):
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            file_name, file_extension = os.path.splitext(file)
            new_file_name = f"{file_name}_{timestamp}{file_extension}"
            dest_path = os.path.join(D_DIR, new_file_name)

        try:
            shutil.copy2(source_path, dest_path)
            print(f"Copied {source_path} to {dest_path}")
        except Exception as e:
            print(f"Error copying {source_path} to {dest_path}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python backup.py <S_DIRectory> <destination_directory>")
        sys.exit(1)
    else :
        print("script starting")
        S_DIRectory = sys.argv[1]
        destination_directory = sys.argv[2]
        print(S_DIRectory , destination_directory)
        backup_files(S_DIRectory, destination_directory)
    
