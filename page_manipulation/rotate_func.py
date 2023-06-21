import cv2
import numpy as np

def rotate_image(image_path, angle):
    """
    Rotates an image by the specified angle.

    Parameters:
    image_path (str): The path to the image file.
    angle (float): The angle by which to rotate the image, in degrees.

    Returns:
    rotated_image: The rotated image.
    """
    # Load the image
    image = cv2.imread(image_path)

    # Check if image loading is successful
    if image is None:
        print('Could not open or find the image')
        return None

    # Get image dimensions
    (height, width) = image.shape[:2]

    # Compute the center of the image
    center = (width / 2, height / 2)

    # Compute the rotation matrix
    matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

    # Get the sine and cosine from the rotation matrix
    abs_cos = abs(matrix[0, 0])
    abs_sin = abs(matrix[0, 1])

    # Compute the new bounding dimensions of the image
    bound_w = int(height * abs_sin + width * abs_cos)
    bound_h = int(height * abs_cos + width * abs_sin)

    # Adjust the rotation matrix to take into account the new dimensions
    matrix[0, 2] += bound_w / 2 - center[0]
    matrix[1, 2] += bound_h / 2 - center[1]

    # Perform the rotation
    rotated_image = cv2.warpAffine(image, matrix, (bound_w, bound_h))

    return rotated_image

# rotated = rotate_image('poster.jpeg', 90)

# # To display the rotated image
# cv2.imshow('Image', rotated)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
