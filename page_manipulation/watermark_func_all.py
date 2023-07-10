import cv2
import numpy as np
from load_pdf import convert_pdf_to_images
from PIL import Image
import os
from images_to_pdf import convert_images_to_pdf


def add_image_watermark(input_file_path, watermark_path, alpha):
    # # Load the image
    # image = cv2.imread(image_path)

    # # Check if image loading is successful
    # if image is None:
    #     print('Could not open or find the image')
    #     return None

    images = convert_pdf_to_images(input_file_path)
    # print(images)
    # Load the watermark
    watermark = cv2.imread(watermark_path, cv2.IMREAD_UNCHANGED)

    # Check if watermark loading is successful
    if watermark is None:
        print('Could not open or find the watermark')
        return None

    # If watermark image has 3 channels, add an alpha channel to it
    if watermark.shape[2] < 4:
        watermark = cv2.cvtColor(watermark, cv2.COLOR_BGR2BGRA)

    # Resize the watermark to match the image size while keeping the aspect ratio
    (h, w) = images[0].shape[:2]
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

    # print(watermark_resized)
    result_list = []
    for img in images:
        # print(type(i))
        # Convert the image to BGRA if it isn't
        if img.shape[2] < 4:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)

        # Blend images
        result = img.copy()
        # print(type(result))
        for j in range(3): # For each color channel
            result[..., j] = (watermark_resized[..., j] * (watermark_resized[..., 3] / 255.0) * alpha +
                            img[..., j] * (1 - (watermark_resized[..., 3] / 255.0) * alpha)).astype(np.uint8)

        result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
        # Convert the OpenCV image representation to PIL image
        result = Image.fromarray(result)
        result_list.append(result)

    print(result_list)

    # Use the function
    # images = ['image1.jpg', 'image2.jpg']
    pdf_data = convert_images_to_pdf(result_list)

    return pdf_data


pdf_data = add_image_watermark('D:\Tasnim Proj\Tasnim Proj\python-pdf-editor-main\python-pdf-editor-main\khanki.pdf', 'D:\Tasnim Proj\Tasnim Proj\python-pdf-editor-main\python-pdf-editor-main\watermark.png', 0.3)

# If you want to save the PDF data to a file later:
with open('output.pdf', 'wb') as f:
    f.write(pdf_data)
# # list of images
# images_list = ['image1.jpg', 'image2.png', 'image3.jpg']

# # convert all images to RGB and save them to a new list
# images = [Image.open(x).convert('RGB') for x in images_list]

# # save images to a pdf file
# images[0].save('output.pdf', save_all=True, append_images=images[1:])




#     return 

# # Use the function like this:
# watermarked = add_image_watermark('C:/Users/ashra/Desktop/Tasnim Proj/python-pdf-editor-main/python-pdf-editor-main/input.png', 'C:/Users/ashra/Desktop/Tasnim Proj/python-pdf-editor-main/python-pdf-editor-main/watermark.png', 0.3)

# # To display the watermarked image
# cv2.imshow('Image', watermarked)
# cv2.imwrite('C:/Users/ashra/Desktop/Tasnim Proj/python-pdf-editor-main/python-pdf-editor-main/pdf_manipulation/output.jpg', watermarked)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
