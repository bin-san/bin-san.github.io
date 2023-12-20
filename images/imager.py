from PIL import Image, ImageOps

def create_mirror_image(input_image_path):
    # Open the image
    original_image = Image.open(input_image_path)

    # Create a mirror copy
    mirror_image = ImageOps.mirror(original_image)

    # Concatenate the original and mirror copy side by side
    result_image = Image.new('RGB', (original_image.width * 2, original_image.height))
    result_image.paste(original_image, (0, 0))
    result_image.paste(mirror_image, (original_image.width, 0))

    original_image = result_image

    mirrored_image = original_image.transpose(Image.FLIP_TOP_BOTTOM)

    # Get the size of the original image
    width, height = original_image.size

    # Create a new image with double the height
    new_image = Image.new('RGB', (width, height * 2))

    # Paste the original image at the top
    new_image.paste(original_image, (0, 0))

    # Paste the mirrored image at the bottom
    new_image.paste(mirrored_image, (0, height))


    return new_image

def main():
    input_image_path = "old-paper.jpg"  # Replace with the actual path to your image
    result_image = create_mirror_image(input_image_path)

    # Save the resulting image
    result_image.save("nold-paper-2.jpg")  # Replace with the desired path to save the result

if __name__ == "__main__":
    main()
