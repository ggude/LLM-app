import pdf2image
import pytesseract
import os

def pdf_to_text(pdf_file):
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

if __name__ == "__main__":
  #pdf_file = "/content/drive/MyDrive/LLM/data/environment_pages290-320.pdf"
  pdf_file = os.getenv(FILE_PATH)
  pages = pdf_to_text(pdf_file)

  