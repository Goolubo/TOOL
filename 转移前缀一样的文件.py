import os

# Define the directories
folder1 = 'D:/Study/ultralytics-main/datasets/road2020-seg/images/val2020'
folder2 = 'D:/jsai/FinalData2/data2_done/black_images'
folder3 = 'D:/Study/ultralytics-main/datasets/road2020-seg/labels/val2020'

# List files in folder1 and folder2
files_folder1 = os.listdir(folder1)
files_folder2 = os.listdir(folder2)

# Extract the first part of the file names in folder1
prefixes_folder1 = {file.split('-')[0] for file in files_folder1 if '-' in file}

# Process the files in folder2
for file2 in files_folder2:
    # Extract the first part of the file name
    prefix_file2 = file2.split('-')[0] if '-' in file2 else None

    # Check if this part matches any prefix in folder1
    if prefix_file2 in prefixes_folder1:
        # Move the file from folder2 to folder3
        os.rename(os.path.join(folder2, file2), os.path.join(folder3, file2))

# You may want to print or log the operation to confirm the files moved
print("Files moved from folder2 to folder3.")
