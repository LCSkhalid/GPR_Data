# -*- coding: utf-8 -*-

import os
import cv2
import numpy as np
from scipy.ndimage import gaussian_filter
from tqdm import tqdm


# Define augmentation functions
def add_noise(image, mean=0, std=0.05):
    """Add Gaussian noise to the image."""
    noise = np.random.normal(mean, std, image.shape)
    noisy_image = image + noise * 255  # Scale noise to image range
    return np.clip(noisy_image, 0, 255).astype(np.uint8)


def time_shift(image, shift):
    """Shift the image horizontally."""
    return np.roll(image, shift, axis=1)


def scale_image(image, zoom_factor):
    """
    Zooms into the image while maintaining the original dimensions.

    Args:
        image (ndarray): Input grayscale image.
        zoom_factor (float): Zoom factor greater than 1 for zoom in.

    Returns:
        ndarray: Zoomed image with the same size as the input.
    """
    height, width = image.shape
    new_height, new_width = int(height / zoom_factor), int(width / zoom_factor)

    # Crop the center of the image
    start_y = (height - new_height) // 2
    start_x = (width - new_width) // 2
    cropped = image[start_y:start_y + new_height, start_x:start_x + new_width]

    # Resize back to original dimensions
    zoomed_image = cv2.resize(cropped, (width, height), interpolation=cv2.INTER_LINEAR)
    return zoomed_image

def rotate_image(image, angle):
    """Rotate the image by a specific angle."""
    height, width = image.shape
    center = (width // 2, height // 2)
    rot_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv2.warpAffine(image, rot_matrix, (width, height), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
    return rotated_image


def flip_image(image, mode):
    """Flip the image: mode=0 (vertical), 1 (horizontal), -1 (both)."""
    return cv2.flip(image, mode)


def elastic_transform(image, alpha, sigma):
    """Apply elastic deformation to the image."""
    random_state = np.random.RandomState(None)
    shape = image.shape

    dx = gaussian_filter((random_state.rand(*shape) * 2 - 1), sigma) * alpha
    dy = gaussian_filter((random_state.rand(*shape) * 2 - 1), sigma) * alpha

    x, y = np.meshgrid(np.arange(shape[1]), np.arange(shape[0]))
    indices = (y + dy).astype(np.float32), (x + dx).astype(np.float32)
    return cv2.remap(image, indices[1], indices[0], interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)


def spectral_shift(image, shift):
    """Shift the image in the frequency domain."""
    f_image = np.fft.fft2(image)
    f_image = np.fft.fftshift(f_image)
    shifted_image = np.roll(f_image, shift, axis=1)
    shifted_image = np.fft.ifftshift(shifted_image)
    return np.abs(np.fft.ifft2(shifted_image)).astype(np.uint8)


# Main function to apply augmentations
def augment_gpr_data(input_folder, output_folder, augmentations):
    """Apply augmentations to GPR data in the input folder."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.jpg')]

    for image_file in tqdm(image_files, desc="Augmenting images"):
        # Load image as grayscale
        image_path = os.path.join(input_folder, image_file)
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        image = cv2.resize(image,(224,224))
        # Apply augmentations
        augmented_images = []
        for func, params in augmentations:
            augmented_image = func(image, **params)
            augmented_images.append(augmented_image)

        # Save augmented images
        base_name = os.path.splitext(image_file)[0]
        for i, aug_image in enumerate(augmented_images):
            aug_file = f"{base_name}_aug_{i + 1}.jpg"
            aug_path = os.path.join(output_folder, aug_file)
            cv2.imwrite(aug_path, aug_image)


# Specify input/output folders and augmentations
input_folder = "Path/to/GPR/images/folder"  # Replace with your GPR images folder
output_folder = "Output/path"  # Replace with your desired output folder

augmentations = [
    (add_noise, {"mean": 0, "std": 0.15}),
    (time_shift, {"shift": 20}),
    (rotate_image, {"angle": 15}),
    (flip_image, {"mode": 1}),
    (elastic_transform, {"alpha": 34, "sigma": 4}),
    (spectral_shift, {"shift": 100}),
]

# Run augmentation
augment_gpr_data(input_folder, output_folder, augmentations)
