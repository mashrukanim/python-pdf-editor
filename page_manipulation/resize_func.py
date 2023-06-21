import cv2

def resize_image(image_path, width, height):
    """
    Resizes an image to the specified width and height.

    Parameters:
    image_path (str): The path to the image file.
    width (int): The new width for the resized image.
    height (int): The new height for the resized image.

    Returns:
    resized_image: The resized image.
    """
    # Load the image
    image = cv2.imread(image_path)

    # Check if image loading is successful
    if image is None:
        print('Could not open or find the image')
        return None

    # Resize the image
    resized_image = cv2.resize(image, (width, height))

    return resized_image


# resized = resize_image('poster.jpeg', 240, 240)

# # To display the resized image
# cv2.imshow('Image', resized)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
