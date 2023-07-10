from pdf2image import convert_from_path
import numpy as np
import cv2

def convert_pdf_to_images(pdf_path):
    """
    Converts a PDF file into images.

    Parameters:
    pdf_path (str): The path to the PDF file.
    output_folder (str): The path to the folder where images should be saved.

    Returns:
    None
    """
    # Convert pages into images
    pages = convert_from_path(pdf_path)
    # print(type(pages))
    img_list = []
    # Save each page as an image
    for i, page in enumerate(pages):
        # image_name = f'{output_folder}/output_{i}.png'
        # print(i)
        img = np.array(page)
        img_list.append(img)
        # cv2.imshow("imgae",img)
        # cv2.waitKey(0)
        # print(type(page))
        # page.save(image_name, 'PNG')
    return img_list

# print(convert_pdf_to_images('D:\Tasnim Proj\Tasnim Proj\python-pdf-editor-main\python-pdf-editor-main\khanki.pdf', 'D:\Tasnim Proj\Tasnim Proj\python-pdf-editor-main\python-pdf-editor-main\page_images_outputs'))
