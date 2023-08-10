import pdf2image
import pytesseract
import os

def Singlepdf_to_text(pdf_file):
  """Converts an image-only PDF file to text.

  Args:
    pdf_file: The path to the PDF file to convert.

  Returns:
    The text content of the PDF file.
  """

  images = pdf2image.convert_from_path(pdf_file)
  text = ""
  pages=[]
  for image in images:
    pages.append(pytesseract.image_to_string(image))
    #text += pytesseract.image_to_string(image)
    #print(text)
  return pages

  #pdf_file = "/content/drive/MyDrive/LLM/data/environment_pages290-320.pdf"
  pdf_file = os.getenv(FILE_PATH)
  pages = Singlepdf_to_text(pdf_file)

def Multiplepdf_to_text(pdf_files):
    """Converts a list of image-only PDF files to text
    
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

    # Read PDF file paths from environment variable and split by semicolon
    pdf_files = os.environ.get("PDF_FILES", "").split(";")
    
    if not pdf_files or not pdf_files[0]:
        print("No PDF files provided in the PDF_FILES environment variable.")
    else:
        texts = Multiplepdf_to_text(pdf_files)
    """
        # Print texts for each PDF
        for pdf_file, pages in texts.items():
            print(f"\nText from {pdf_file}:\n")
            for page in pages:
                print(page)
    """
  