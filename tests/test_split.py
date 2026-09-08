from operations.split import split_pdf
import os

def main():
    print("Split PDF Test")

    file = os.listdir("test_pdfs")[0]

    file = os.path.join("test_pdfs", file)

    split_pdf(file)


if __name__ == "__main__":
    main()