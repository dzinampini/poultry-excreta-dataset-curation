import os
import json
import re

def clean_folder_name(name):
    # Convert to lowercase
    name = name.lower()
    # Replace special characters (except letters, numbers, and spaces) with dash
    name = re.sub(r'[^a-z0-9\s-]', '-', name)
    # Replace spaces with dash
    name = name.replace(' ', '-')
    # Remove consecutive dashes
    name = re.sub(r'-+', '-', name)
    # Remove leading/trailing dashes
    name = name.strip('-')
    return name

def create_folders_from_json(json_data):
    # Create the main dataset folder if it doesn't exist
    dataset_folder = "dataset"
    os.makedirs(dataset_folder, exist_ok=False)
    
    # Iterate through each disease and create a folder
    for disease in json_data:
        # Get the disease name and create a valid folder name
        folder_name = clean_folder_name(disease["name"])  # Replace any slashes that might cause issues
        folder_path = os.path.join(dataset_folder, folder_name)
        
        # Create the folder
        os.makedirs(folder_path, exist_ok=True)
        print(f"Created folder: {folder_path}")
        
        # Optional: Create a JSON file with the disease info in its folder
        disease_file = os.path.join(folder_path, "disease_info.json")
        with open(disease_file, 'w') as f:
            json.dump(disease, f, indent=4)
        
    print("\nAll folders created successfully!")


def create_folders_from_json_file(json_file):
    # Load JSON data from file
    with open(json_file) as f:
        data = json.load(f)
    
    create_folders_from_json(data)

# Then call it with your JSON file
create_folders_from_json_file("diseases.json")
