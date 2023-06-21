import cv2
import numpy as np

def add_image_watermark(image_path, watermark_path, alpha):
    # Load the image
    image = cv2.imread(image_path)

    # Check if image loading is successful
    if image is None:
        print('Could not open or find the image')
        return None

    # Load the watermark
    watermark = cv2.imread(watermark_path, cv2.IMREAD_UNCHANGED)

    # Check if watermark loading is successful
    if watermark is None:
        print('Could not open or find the watermark')
        return None

    # Resize the watermark to match the image size while keeping the aspect ratio
    (h, w) = image.shape[:2]
    (h_w, w_w) = watermark.shape[:2]

    # Calculate scale factors
    scale_w = w / w_w
    scale_h = h / h_w
    scale = min(scale_w, scale_h)

    # Resize watermark
    watermark = cv2.resize(watermark, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)

    # Create an empty image with the same size as the original image
    watermark_resized = np.zeros((h, w, 4), dtype=np.uint8)

    # Place the scaled watermark in the center of the empty image
    start_y = (h - watermark.shape[0]) // 2
    start_x = (w - watermark.shape[1]) // 2
    watermark_resized[start_y:start_y+watermark.shape[0], start_x:start_x+watermark.shape[1]] = watermark

    # Convert the image to BGRA if it isn't
    if image.shape[2] < 4:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)

    # Blend images
    result = image.copy()
    for i in range(3): # For each color channel
        result[..., i] = (watermark_resized[..., i] * (watermark_resized[..., 3] / 255.0) * alpha +
                          image[..., i] * (1 - (watermark_resized[..., 3] / 255.0) * alpha)).astype(np.uint8)

    return result



# # Use the function like this:
# watermarked = add_image_watermark('C:/Users/Mashruk Anim/Desktop/func/input.png', 'C:/Users/Mashruk Anim/Desktop/func/watermark.png', 0.3)

# # To display the watermarked image
# cv2.imshow('Image', watermarked)
# cv2.imwrite('output.jpg', watermarked)
# cv2.waitKey(0)
# cv2.destroyAllWindows()