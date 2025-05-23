import os


def count_files_in_folders(dataset_path="dataset"):
    # Dictionary to store folder names and their file counts
    folder_counts = {}
    total_files = 0 
    
    # Check if dataset folder exists
    if not os.path.exists(dataset_path):
        print(f"Error: Dataset folder '{dataset_path}' not found!")
        return
    
    # Iterate through each folder in the dataset
    for folder_name in os.listdir(dataset_path):
        folder_path = os.path.join(dataset_path, folder_name)
        
        # Only process directories (skip files)
        if os.path.isdir(folder_path):
            # Count files in the folder (excluding subdirectories)
            file_count = len([
                f for f in os.listdir(folder_path) 
                if os.path.isfile(os.path.join(folder_path, f))
            ])
            folder_counts[folder_name] = file_count
    
    # Print results
    print("File counts per folder:")
    print(f"-------------------------------------------")
    for folder, count in folder_counts.items():
        actual_count = count - 1
        total_files = total_files + actual_count
        print(f"{folder}: {actual_count} images")

    
    return total_files

# Run the function
total_files = count_files_in_folders()
print(f"-------------------------------------------")
print(f"Total files in all folders: {total_files} images")