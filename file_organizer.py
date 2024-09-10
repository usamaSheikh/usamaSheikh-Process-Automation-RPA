import os
import shutil
import datetime

def organize_files():
    download_dir = "path_to_download_folder"
    target_dir = "path_to_target_folder"  # Replace with the folder where files will be organized

    # Get all downloaded PDF files
    files = [f for f in os.listdir(download_dir) if f.endswith('.pdf')]

    for file in files:
        # Generate a new name based on the current date
        new_name = f"report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        source_path = os.path.join(download_dir, file)
        target_path = os.path.join(target_dir, new_name)
        
        # Move and rename the file
        shutil.move(source_path, target_path)
        print(f"File {file} moved to {target_path}")

if __name__ == "__main__":
    organize_files()
