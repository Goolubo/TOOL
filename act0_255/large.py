import cv2
import numpy as np


def find_connected_areas_binary(img, connectivity=2):
    """
    Find connected areas in a binary image and mark them as a single value (255).

    :param img: Input binary image (numpy array) with pixel values 0 or 255.
    :param connectivity: Pixel range to consider for connecting areas (default is 5).
    :return: Binary image with connected areas marked as 255.
    """
    labeled_img = np.zeros_like(img)

    # Check each pixel
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i, j] == 255:
                # Define the neighborhood
                min_row = max(0, i - connectivity)
                max_row = min(img.shape[0], i + connectivity + 1)
                min_col = max(0, j - connectivity)
                max_col = min(img.shape[1], j + connectivity + 1)

                # Check if there is any other white pixel in the neighborhood
                if np.any(img[min_row:max_row, min_col:max_col] == 255):
                    # Mark the pixel and its neighborhood as part of the connected area
                    labeled_img[min_row:max_row, min_col:max_col] = 255

    return labeled_img

def process_binary_image(image_path, output_path):
    # Read the image in grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Check if the image is loaded properly
    if img is None:
        print("Error: Image could not be loaded.")
        return None

    # Find connected areas and mark them in binary
    connected_areas_binary = find_connected_areas_binary(img)

    # Save the binary connected areas image
    cv2.imwrite(output_path, connected_areas_binary)

    return output_path

# Example usage with the binary processing function
binary_image_path = "D:/jsai/1/24-out_ori_6.png"
binary_output_path = "D:/jsai/1/24.png"
binary_result = process_binary_image(binary_image_path, binary_output_path)

print("Binary processed image saved at:", binary_result)



