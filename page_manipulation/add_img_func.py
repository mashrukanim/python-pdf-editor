import cv2

def add_image_to_image(background_path, overlay_path, position=(0,0)):
    # Load the background image
    background = cv2.imread(background_path)

    # Check if background image loading is successful
    if background is None:
        print('Could not open or find the background image')
        return None

    # Load the overlay image
    overlay = cv2.imread(overlay_path)

    # Check if overlay image loading is successful
    if overlay is None:
        print('Could not open or find the overlay image')
        return None

    # Get the dimensions of both images
    (h_b, w_b) = background.shape[:2]
    (h_o, w_o) = overlay.shape[:2]

    # Calculate the bounds of the region that will be occupied by the overlay
    x_start = position[0]
    x_end = min(position[0] + w_o, w_b)
    y_start = position[1]
    y_end = min(position[1] + h_o, h_b)

    # Crop the overlay if necessary
    if x_end - x_start < w_o or y_end - y_start < h_o:
        overlay = overlay[:y_end-y_start, :x_end-x_start]

    # Place the overlay on the background at the specified (or modified) position
    background[y_start:y_end, x_start:x_end] = overlay

    return background

# Use the function like this:
result = add_image_to_image('C:/Users/Mashruk Anim/Desktop/func/input.png', 'C:/Users/Mashruk Anim/Desktop/func/add_img.jpg', (100, 50))

# Display the image
cv2.imshow('Image', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
