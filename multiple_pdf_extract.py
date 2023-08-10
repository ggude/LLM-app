import os
import pdf2image
import pytesseract

def pdf_to_text(pdf_files):
    """Converts a list of image-only PDF files to text.
    
    Args:
        pdf_files: A list of paths to the PDF files to convert.

    Returns:
        A dictionary where the key is the PDF file path and the value is the list of text for each page.
    """
    
    all_texts = {}
    
    for pdf_file in pdf_files:
        images = pdf2image.convert_from_path(pdf_file)
        pages = [pytesseract.image_to_string(image) for image in images]
        all_texts[pdf_file] = pages

    return all_texts

if __name__ == "__main__":
    # Read PDF file paths from environment variable and split by semicolon
    pdf_files = os.environ.get("PDF_FILES", "").split(";")
    
    if not pdf_files or not pdf_files[0]:
        print("No PDF files provided in the PDF_FILES environment variable.")
    else:
        texts = pdf_to_text(pdf_files)

        # Print texts for each PDF
        for pdf_file, pages in texts.items():
            print(f"\nText from {pdf_file}:\n")
            for page in pages:
                print(page)
