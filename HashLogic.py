import imagehash
from datetime import datetime
import os


def compare_images(image_folder):

    error_filename = f"Error_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(error_filename, "w") as error_file:

        for filename in os.listdir(image_folder):
            image1_path = os.path.join(image_folder, filename)
            image2_path = os.path.join(image_folder, "another_folder", filename)

            if os.path.isfile(image2_path):
                hash1 = imagehash.average_hash(image1_path)
                hash2 = imagehash.average_hash(image2_path)

                if hash1 - hash2 < threshold:
                    error_file.write(f"Image comparison error: {image2_path}\n")

    print(f"An error file named {error_filename} has been created.")


# Example usage
image_folder = "path_to_images_folder"
threshold = 5
compare_images(image_folder)
