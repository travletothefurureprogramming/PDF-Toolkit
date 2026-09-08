from operations.extract_text import extarct_text
import os

def main():
    print("Split PDF Test")

    file = os.listdir("test_pdfs")[0]

    file = os.path.join("test_pdfs", file)

    extarct_text(file)


if __name__ == "__main__":
    main()