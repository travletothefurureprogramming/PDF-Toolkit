from operations.pdf_to_image import to_png
import os

def main():
    print("PDF to Image Test")

    file = os.listdir("test_pdfs")[0]

    file = os.path.join("test_pdfs", file)

    to_png(file,1)


if __name__ == "__main__":
    main()