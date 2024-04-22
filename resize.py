import os
from PIL import Image

def convert_and_resize_images(input_folder, output_folder, size=(256, 256), output_format='PNG'):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all files in the input folder
    files = os.listdir(input_folder)

    # Loop through each file in the input folder
    for file_name in files:
        if file_name.endswith(('.webp')):
            image_path = os.path.join(input_folder, file_name)
            img = Image.open(image_path)
            file_name_no_extension = os.path.splitext(file_name)[0]
            output_path = os.path.join(output_folder, f"{file_name_no_extension}.png")
            img.save(output_path, format=output_format)
            print(f"Converted {file_name} -> {file_name_no_extension}.png")
        # Check if the file is an image
        if file_name.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            # Open the image
            image_path = os.path.join(input_folder, file_name)
            img = Image.open(image_path)

            # Convert the image to RGB mode (if it's not already in RGB)
            if img.mode != 'RGB':
                img = img.convert('RGB')

            # Resize the image
            img_resized = img.resize(size)

            # Get the file name without extension
            file_name_no_extension = os.path.splitext(file_name)[0]

            # Save the resized image
            output_path = os.path.join(output_folder, f"{file_name_no_extension}.png")
            img_resized.save(output_path, format=output_format)

            print(f"Converted and resized {file_name} -> {file_name_no_extension}.png")

def convert_png_to_jpg(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all files in the input folder
    files = os.listdir(input_folder)

    # Loop through each file in the input folder
    for file_name in files:
        # Check if the file is a PNG image
        if file_name == "ljump1.webp":
            # Open the PNG image
            image_path = os.path.join(input_folder, file_name)
            img = Image.open(image_path)

            # Get the file name without extension
            file_name_no_extension = os.path.splitext(file_name)[0]

            # Save the image as JPG
            output_path = os.path.join(output_folder, f"{file_name_no_extension}.jpg")
            img.convert('RGB').save(output_path)

            print(f"Converted {file_name} to {file_name_no_extension}.jpg")

if __name__ == "__main__":

    input_folder = input("Enter the path to the folder containing images: ")
    output_folder = input("Enter the path to the output folder: ")

    # Call the function to convert and resize images
    #convert_png_to_jpg(input_folder,output_folder)
    convert_and_resize_images(input_folder, output_folder)