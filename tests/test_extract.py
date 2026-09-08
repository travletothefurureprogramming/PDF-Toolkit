from operations.extract import extract_pages
import os

def main():
    print("Split PDF Test")

    file = os.listdir("test_pdfs")[0]

    file = os.path.join("test_pdfs", file)

    extract_pages(file,"1-2")


if __name__ == "__main__":
    main()