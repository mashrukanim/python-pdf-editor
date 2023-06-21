import cv2

def add_textbox(image_path, text, origin, font_scale, color, thickness):
    """
    Adds a textbox to an image.

    Parameters:
    image_path (str): The path to the image file.
    text (str): The text to be added.
    origin (tuple): The bottom-left corner of the text string in the image (x, y).
    font_scale (float): Font scale factor that is multiplied by the font-specific base size.
    color (tuple): Text color in BGR.
    thickness (int): Thickness of the lines used to draw a text.

    Returns:
    None
    """
    # Load the image
    image = cv2.imread(image_path)

    # Check if image loading is successful
    if image is None:
        print('Could not open or find the image')
        return None

    # Define the font
    font = cv2.FONT_HERSHEY_SIMPLEX

    # Add the text
    cv2.putText(image, text, origin, font, font_scale, color, thickness, cv2.LINE_AA)

    # Show the image
    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# add_textbox('poster.jpeg', 'Hello, World!', (50, 50), 1, (255, 0, 0), 2)
