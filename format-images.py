import os
from PIL import Image
from pathlib import Path

def process_images(dataset_path="dataset", output_size=(250, 250)):
    # Supported image extensions
    supported_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')
    
    # Check if dataset folder exists
    if not os.path.exists(dataset_path):
        print(f"Error: Dataset folder '{dataset_path}' not found!")
        return
    
    # Process each folder
    for folder_name in os.listdir(dataset_path):
        folder_path = os.path.join(dataset_path, folder_name)
        
        if not os.path.isdir(folder_path):
            continue
            
        print(f"\nProcessing folder: {folder_name}")
        
        # Process each file in the folder
        i = 0
        for filename in os.listdir(folder_path):
            i += 1
            file_path = os.path.join(folder_path, filename)
            
            # Skip directories and non-image files
            if not os.path.isfile(file_path):
                continue
                
            file_ext = Path(filename).suffix.lower()
            if file_ext not in supported_extensions:
                continue
                
            try:
                # Open the image
                with Image.open(file_path) as img:
                    # Convert to RGB if needed (for PNG with transparency)
                    if img.mode in ('RGBA', 'P'):
                        img = img.convert('RGB')
                    
                    # Resize the image while maintaining aspect ratio
                    img.thumbnail(output_size, Image.Resampling.LANCZOS)
                    
                    # Create a new 250x250 canvas with white background
                    new_img = Image.new('RGB', output_size, (255, 255, 255))
                    # Paste the resized image centered
                    new_img.paste(img, (
                        (output_size[0] - img.size[0]) // 2,
                        (output_size[1] - img.size[1]) // 2
                    ))
                    
                    # Generate new filename (same name but with .jpg extension)
                    new_filename = Path(folder_name+str(i)).stem + '.jpg'
                    new_filepath = os.path.join(folder_path, new_filename)
                    
                    # Save as JPG with quality=90
                    new_img.save(new_filepath, 'JPEG', quality=90)
                    
                    print(f"Converted: {filename} → {new_filename} ({img.size} → {output_size})")
                    
                    # Remove original file if it's not already a JPG
                    if file_ext != '.jpg' and file_ext != '.jpeg':
                        os.remove(file_path)

                    if new_filepath != file_path:
                        os.remove(file_path)
                        print(f"Deleted original: {filename}")
                        
            except Exception as e:
                print(f"Error processing {filename}: {str(e)}")

if __name__ == "__main__":
    process_images()