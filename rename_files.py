import os

# Path to the folder containing the files
path_list = ['exciting', 'fearful', 'neutral', 'relaxing', 'sad', 'tense']

for folder_path in path_list:
    # List all files in the folder
    files = os.listdir(folder_path)

    # Iterate over the files and rename them
    for i, file in enumerate(files, start=1):
        # New file name folder_path the format "index.mp4"
        new_name = f"{folder_path}_{i}.mp4"
        
        # Current file path
        current_path = os.path.join(folder_path, file)
        
        # New file path
        new_path = os.path.join(folder_path, new_name)
        
        # Rename the file
        os.rename(current_path, new_path)

print("Files renamed successfully!")
