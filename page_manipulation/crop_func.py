import cv2

def crop_image(image_path, start_x, start_y, end_x, end_y):
    """
    Crops an image given the start and end (x,y) coordinates.

    Parameters:
    image_path (str): The path to the image file.
    start_x (int): The x-coordinate of the start point.
    start_y (int): The y-coordinate of the start point.
    end_x (int): The x-coordinate of the end point.
    end_y (int): The y-coordinate of the end point.

    Returns:
    cropped_image: The cropped image.
    """
    # Load the image
    image = cv2.imread(image_path)

    # Check if image loading is successful
    if image is None:
        print('Could not open or find the image')
        return None

    # Crop the image
    cropped_image = image[start_y:end_y, start_x:end_x]

    return cropped_image

cropped = crop_image('poster.jpeg', 100, 100, 200, 200)

# # To display the cropped image
# cv2.imshow('Image', cropped)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
