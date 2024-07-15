import cv2
import numpy as np
import os

def fill_connected_regions(image):
    """
    Fill connected regions in the image where enclosed areas containing pixel value 0 will be filled with 255.

    :param image: Input binary image (numpy array) with pixel values 0 or 255.
    :return: Image with filled connected regions.
    """
    # Find all contours in the image
    contours, _ = cv2.findContours(image, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

    # Create a mask for filling the contours
    mask = np.zeros_like(image)

    for cnt in contours:
        # Check if the contour is closed
        if cv2.contourArea(cnt) > 0:
            cv2.drawContours(mask, [cnt], -1, 255, -1)

    # Fill the areas in the original image where mask is white and original image is black (0)
    filled_image = np.where((mask == 255) & (image == 0), 255, image)

    return filled_image

def process_images_in_folder(folder_path, output_folder):
    for filename in os.listdir(folder_path):
        if filename.endswith(".png"):
            # Read the image
            image_path = os.path.join(folder_path, filename)
            img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

            if img is not None:
                # Process the image
                processed_img = fill_connected_regions(img)

                # Save the processed image
                output_path = os.path.join(output_folder, filename)
                cv2.imwrite(output_path, processed_img)
                print(f"Processed {filename}")

# Example usage
input_folder = "D:/jsai/1"  # Replace with the path to your folder
output_folder = "D:/jsai/1"  # Replace with the path to the output folder
process_images_in_folder(input_folder, output_folder)

