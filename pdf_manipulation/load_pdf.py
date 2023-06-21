from pdf2image import convert_from_path

def convert_pdf_to_images(pdf_path, output_folder):
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

    # Save each page as an image
    for i, page in enumerate(pages):
        image_name = f'{output_folder}/output_{i}.png'
        page.save(image_name, 'PNG')

# convert_pdf_to_images('khanki.pdf', 'pdf_images')
