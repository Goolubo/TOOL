# from PIL import Image, ImageDraw
# import os
#
#
# def generate_black_images(image_path):
#     # Open the original image to get its resolution
#     original_image = Image.open(image_path)
#     width, height = original_image.size
#
#     # Create eight black images with the same resolution
#     black_images = [Image.new('RGB', (width, height), color='black') for _ in range(8)]
#
#     # Generate the new image names
#     image_name = os.path.splitext(os.path.basename(image_path))[0]
#
#     for i, black_image in enumerate(black_images):
#         # Save the black images
#         new_image_name = f"{image_name}_{i}.jpg"
#         black_image.save(new_image_name)
#
# def process_txt_file(image_path, txt_path):
#     # Open the original image to get its resolution
#     original_image = Image.open(image_path)
#     width, height = original_image.size
#
#     # Read the labels and float data from the txt file
#     with open(txt_path, 'r') as file:
#         lines = file.readlines()
#
#     for line in lines:
#         data = line.strip().split()
#         label = int(data[0])
#
#         # Loop through the float data
#         for i in range(1, len(data), 3):
#             x, y, side_px = map(float, data[i:i+3])
#
#             # Calculate the actual coordinates in the image
#             x = max(0, min(1, x)) * width
#             y = max(0, min(1, y)) * height
#
#             # Calculate the region to set to white
#             x1 = int(max(0, x - side_px / 2))
#             y1 = int(max(0, y - side_px / 2))
#             x2 = int(min(width, x + side_px / 2))
#             y2 = int(min(height, y + side_px / 2))
#
#             # Open the corresponding black image and set the region to white
#             image_name = os.path.splitext(os.path.basename(image_path))[0]
#             black_image_path = f"{image_name}_{label}.jpg"
#             black_image = Image.open(black_image_path)
#             draw = ImageDraw.Draw(black_image)
#             draw.rectangle([x1, y1, x2, y2], fill='white')
#             black_image.save(black_image_path)
#
#
# if __name__ == "__main__":
#     # Specify the path to the folder containing the images and txt files
#     # folder_path = "D:/jsai/FinalData2/data2jpg_add_txt"
#     folder_path = "D:/桌面/新建文件夹"
#
#     # Iterate through all files in the folder
#     for file_name in os.listdir(folder_path):
#         file_path = os.path.join(folder_path, file_name)
#
#         # Check if the file is a jpg image
#         if file_name.lower().endswith(".jpg"):
#             generate_black_images(file_path)
#         elif file_name.lower().endswith(".txt"):
#             # Find the corresponding image file
#             image_name = os.path.splitext(file_name)[0]
#             image_path = os.path.join(folder_path, f"{image_name}.jpg")
#
#             # Process the txt file
#             process_txt_file(image_path, file_path)



# from PIL import Image, ImageDraw
# import os
#
# def generate_black_images(image_path, output_folder):
#     # Open the original image to get its resolution
#     original_image = Image.open(image_path)
#     width, height = original_image.size
#
#     # Create eight black images with the same resolution
#     black_images = [Image.new('RGB', (width, height), color='black') for _ in range(8)]
#
#     # Generate the new image names
#     image_name = os.path.splitext(os.path.basename(image_path))[0]
#
#     for i, black_image in enumerate(black_images):
#         # Save the black images to the specified output folder
#         new_image_name = f"{image_name}_{i}.jpg"
#         new_image_path = os.path.join(output_folder, new_image_name)
#         black_image.save(new_image_path)
#
# def process_txt_file(image_path, txt_path):
#     # Open the original image to get its resolution
#     original_image = Image.open(image_path)
#     width, height = original_image.size
#
#     # Read the labels and float data from the txt file
#     with open(txt_path, 'r') as file:
#         lines = file.readlines()
#
#     for line in lines:
#         data = line.strip().split()
#         label = int(data[0])
#
#         # Loop through the float data
#         for i in range(1, len(data), 3):
#             x, y, side_px = map(float, data[i:i+3])
#
#             # Calculate the actual coordinates in the image
#             x = max(0, min(1, x)) * width
#             y = max(0, min(1, y)) * height
#
#             # Calculate the region to set to white
#             x1 = int(max(0, x - side_px / 2))
#             y1 = int(max(0, y - side_px / 2))
#             x2 = int(min(width, x + side_px / 2))
#             y2 = int(min(height, y + side_px / 2))
#
#             # Open the corresponding black image and set the region to white
#             image_name = os.path.splitext(os.path.basename(image_path))[0]
#             black_image_path = os.path.join(output_folder, f"{image_name}_{label}.jpg")
#             black_image = Image.open(black_image_path)
#             draw = ImageDraw.Draw(black_image)
#             draw.rectangle([x1, y1, x2, y2], fill='white')
#             black_image.save(black_image_path)
#
# if __name__ == "__main__":
#     # Specify the path to the folder containing the images and txt files
#     folder_path = "D:/jsai/FinalData2/data2jpg_add_txt"
#     output_folder = "D:/jsai/FinalData2/data2jpg_add_txt/black_images"  # Specify the folder for saving black images
#
#     # Iterate through all files in the folder
#     for file_name in os.listdir(folder_path):
#         file_path = os.path.join(folder_path, file_name)
#
#         # Check if the file is a jpg image
#         if file_name.lower().endswith(".jpg"):
#             generate_black_images(file_path, output_folder)
#         elif file_name.lower().endswith(".txt"):
#             # Find the corresponding image file
#             image_name = os.path.splitext(file_name)[0]
#             image_path = os.path.join(folder_path, f"{image_name}.jpg")
#
#             # Process the txt file
#             process_txt_file(image_path, file_path)


from PIL import Image, ImageDraw
import os

def generate_black_images(image_path, output_folder):
    # Open the original image to get its resolution
    original_image = Image.open(image_path)
    width, height = original_image.size

    # Create eight black images with the same resolution
    black_images = [Image.new('RGB', (width, height), color='black') for _ in range(8)]

    # Generate the new image names
    image_name = os.path.splitext(os.path.basename(image_path))[0]

    for i, black_image in enumerate(black_images):
        # Save the black images to the specified output folder
        new_image_name = f"{image_name}_{i}.jpg"
        new_image_path = os.path.join(output_folder, new_image_name)
        black_image.save(new_image_path)

def process_txt_file(image_path, txt_path, output_folder):
    # Open the original image to get its resolution
    original_image = Image.open(image_path)
    width, height = original_image.size

    # Read the labels and float data from the txt file
    with open(txt_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split()
        label = int(data[0])

        # Loop through the float data
        for i in range(1, len(data), 3):
            x, y, side_px = map(float, data[i:i+3])

            # Calculate the actual coordinates in the image
            x = max(0, min(1, x)) * width
            y = max(0, min(1, y)) * height

            # Calculate the region to set to white
            x1 = int(max(0, x - side_px / 2))
            y1 = int(max(0, y - side_px / 2))
            x2 = int(min(width, x + side_px / 2))
            y2 = int(min(height, y + side_px / 2))

            # Open the corresponding black image and set the region to white
            image_name = os.path.splitext(os.path.basename(image_path))[0]
            black_image_path = os.path.join(output_folder, f"{image_name}_{label}.jpg")
            black_image = Image.open(black_image_path)
            draw = ImageDraw.Draw(black_image)
            draw.rectangle([x1, y1, x2, y2], fill='white')
            black_image.save(black_image_path)

if __name__ == "__main__":
    # Specify the path to the folder containing the images and txt files
    folder_path = "D:/jsai/FinalData2/data2jpg_add_txt"
    output_folder = "D:/jsai/FinalData2/data2jpg_add_txt/black_images"  # Specify the folder for saving black images
    # folder_path = "D:/桌面/张"
    # output_folder = "D:/桌面/张/black_images"

    # Get a sorted list of files in the folder based on numeric part of the filename
    files = sorted(os.listdir(folder_path),
                   key=lambda x: int(''.join(filter(str.isdigit, x))) if any(char.isdigit() for char in x) else 0)

    # Iterate through all files in the folder
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)

        # Check if the file is a jpg image
        if file_name.lower().endswith(".jpg"):
            generate_black_images(file_path, output_folder)
        elif file_name.lower().endswith(".txt"):
            # Find the corresponding image file
            image_name = os.path.splitext(file_name)[0]
            image_path = os.path.join(folder_path, f"{image_name}.jpg")

            # Process the txt file
            process_txt_file(image_path, file_path, output_folder)

    # Get a sorted list of files in the folder
    # files = sorted(os.listdir(folder_path))
    #
    # # Iterate through all files in the folder
    # for file_name in files:
    #     file_path = os.path.join(folder_path, file_name)
    #
    #     # Check if the file is a jpg image
    #     if file_name.lower().endswith(".jpg"):
    #         generate_black_images(file_path, output_folder)
    #     elif file_name.lower().endswith(".txt"):
    #         # Find the corresponding image file
    #         image_name = os.path.splitext(file_name)[0]
    #         image_path = os.path.join(folder_path, f"{image_name}.jpg")
    #
    #         # Process the txt file
    #         process_txt_file(image_path, file_path, output_folder)
