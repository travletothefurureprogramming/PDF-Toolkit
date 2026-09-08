
from operations.merge import merge_files
import os


def main():
    print("Merge Test")

    files = [
        os.path.join("test_pdfs", file)
        for file in os.listdir("test_pdfs")
        if file.lower().endswith(".pdf")
    ]

    merge_files(files)


if __name__ == "__main__":
    main()