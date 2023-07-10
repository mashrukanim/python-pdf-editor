import img2pdf
from PIL import Image
import io


import img2pdf
from PIL import Image
from io import BytesIO

def convert_images_to_pdf(images):
    # Convert each image to RGB
    rgb_images = []
    for image in images:
        if image.mode == "RGBA":
            rgb_image = Image.new("RGB", image.size, (255, 255, 255))  # 3 is the alpha channel
            rgb_image.paste(image, mask=image.split()[3])  
            rgb_images.append(rgb_image)
        else:
            rgb_images.append(image)

    # Convert images to PDF; if images have different sizes, resize is needed
    pdf_bytes = img2pdf.convert([img_to_bytes(img) for img in rgb_images], with_pdfrw=False)
    return pdf_bytes

def img_to_bytes(img):
    # Helper function to convert PIL Image to bytes
    byte_arr = BytesIO()
    img.save(byte_arr, format='PNG')
    return byte_arr.getvalue()

# import img2pdf

# def convert_images_to_pdf(images):
#     pdf_bytes = img2pdf.convert(images)
#     return pdf_bytes

# import img2pdf
# from PIL import Image

# def convert_images_to_pdf(images):
#     # Convert each image to RGB
#     rgb_images = []
#     for image in images:
#         if image.mode == "RGBA":
#             rgb_image = Image.new("RGB", image.size, (255, 255, 255))  # 3 is the alpha channel
#             rgb_image.paste(image, mask=image.split()[3])  
#             rgb_images.append(rgb_image)
#         else:
#             rgb_images.append(image)

#     # Convert images to PDF; if images have different sizes, resize is needed
#     pdf_bytes = img2pdf.convert([img.size for img in rgb_images], with_pdfrw=False)
#     return pdf_bytes

# def convert_images_to_pdf(images):

#     mm_per_inch = 25.4
#     # Convert each image to RGB
#     rgb_images = []
#     for image in images:
#         im = Image.open(image)
#         if im.mode == "RGBA":
#             rgb_image = Image.new("RGB", im.size, (255, 255, 255))
#             rgb_image.paste(im, mask=im.split()[3])  # 3 is the alpha channel
#             rgb_images.append(rgb_image)
#         else:
#             rgb_images.append(im)

#     # Convert images to PDF; if images have different sizes, resize is needed
#     pdf_bytes = img2pdf.convert([img2pdf.A4MM * (im.size[0]/mm_per_inch, im.size[1]/mm_per_inch) for im in rgb_images], rgb_images)
#     return pdf_bytes
