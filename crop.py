# -*- coding: utf-8 -*-

import os
import cv2

def crop_and_save_images(input_folder, output_folder, patch_size=(224, 224)):
    """
    Crops all images in a folder into patches of specified size and saves them with numeric names.

    Args:
        input_folder (str): Path to the folder containing input images.
        output_folder (str): Path to the folder to save cropped patches.
        patch_size (tuple): Size of the patches (width, height).
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.jpg', '.png', '.jpeg'))]
    patch_width, patch_height = patch_size
    patch_count = 1

    for image_file in image_files:
        image_path = os.path.join(input_folder, image_file)
        image = cv2.imread(image_path)

        if image is None:
            print(f"Could not read {image_file}, skipping...")
            continue

        height, width, _ = image.shape

        # Crop patches
        for y in range(0, height, patch_height):
            for x in range(0, width, patch_width):
                # Ensure patch is exactly the specified size
                if x + patch_width <= width and y + patch_height <= height:
                    patch = image[y:y + patch_height, x:x + patch_width]

                    # Save patch
                    patch_name = f"{patch_count:03d}.jpg"
                    patch_path = os.path.join(output_folder, patch_name)
                    cv2.imwrite(patch_path, patch)
                    patch_count += 1

    print(f"Cropped patches saved to {output_folder}. Total patches: {patch_count - 1}")

# Example usage
input_folder = "Path/to/GPR_Profiles"
output_folder = "Output/path"
crop_and_save_images(input_folder, output_folder)
