import os
import shutil

def extract_pngs_and_remove_folders(root_folder):
    # Recursively iterate over folders and files in the root folder
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            if file.endswith((".png",".jpg")):
                # Construct the old and new file paths
                old_file_path = os.path.join(root, file)
                category_folder = os.path.basename(root)
                new_file_name = f"{category_folder}_{file}"

                directory = os.path.dirname(root)
                new_file_path = os.path.join(directory, new_file_name)

                # Rename the PNG file
                os.rename(old_file_path, new_file_path)
                print(f"Renamed: {old_file_path} -> {new_file_path}")
    
    # Remove empty category folders
    for root, dirs, files in os.walk(root_folder, topdown=False):
        for dir in dirs:
            folder_path = os.path.join(root, dir)
            if not os.listdir(folder_path):  # Check if folder is empty
                os.rmdir(folder_path)
                print("Removed folder:", folder_path)

# Example usage:
root_folder = input("Give dataset folder (e.g. dataset256/train): ")
extract_pngs_and_remove_folders(root_folder)