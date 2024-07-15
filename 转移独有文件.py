import os
import shutil


def move_extra_files(source_folder1,
                     source_folder2,
                     destination_folder):
    """
    Move files from source_folder1 to destination_folder that are not present in source_folder2.
    """
    # List all files in both source folders
    files_in_folder1 = set(os.listdir(source_folder1))
    files_in_folder2 = set(os.listdir(source_folder2))

    # Find files that are in folder1 but not in folder2
    extra_files = files_in_folder1 - files_in_folder2

    # Ensure the destination folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Move each extra file to the destination folder
    for file in extra_files:
        shutil.move(os.path.join(source_folder1, file), os.path.join(destination_folder, file))

    return extra_files

# Example usage
# Replace the folder paths with the actual paths on your system
move_extra_files("D:/Study/ultralytics-main/datasets/road2020/images/train2023(1)",
                 "D:/Study/ultralytics-main/datasets/road2020/images/train2023",
                 "D:/Study/ultralytics-main/datasets/road2020/images/val2023(1)")
