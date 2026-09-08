import questionary
from os import path
from tkinter.filedialog import (
    askopenfilenames,
    asksaveasfilename,
    askopenfilename,
    askdirectory,
)

from operations.extract import extract_pages
from operations.split import split_pdf
from operations.merge import merge_files
from operations.convert import to_png

import argparse

VERSION = "1.0.0"

parser = argparse.ArgumentParser(
    description="PDF Toolkit - A simple PDF utility for Python"
)

parser.add_argument(
    "--version",
    action="version",
    version=f"PDF Toolkit {VERSION}"
)

args = parser.parse_args()

def main():
    print(
        "╭──────────────────────────────────╮\n"
        "|           PDF Toolkit            |\n"
        "╰──────────────────────────────────╯\n"
    )

    while True:
        operation = questionary.select(
            "Choose an operation:",
            choices=[
                "Merge PDFs",
                "PDF → Image",
                "Split PDF",
                "Extract Pages",
                "Exit",
            ],
        ).ask()

        # User closed the Questionary prompt
        if operation is None or operation == "Exit":
            print("\nGoodbye!")
            break

        # --------------------------------------------------
        # Merge PDFs
        # --------------------------------------------------
        elif operation == "Merge PDFs":
            print("\nMerge PDFs")

            files = askopenfilenames(
                title="Select PDF files to merge",
                filetypes=[("PDF files", "*.pdf")],
            )

            if not files:
                print("No files selected.")
                continue

            output = asksaveasfilename(
                title="Save merged PDF",
                defaultextension=".pdf",
                filetypes=[("PDF files", "*.pdf")],
            )

            if not output:
                print("Output location not selected.")
                continue

            try:
                merge_files(files, output)
                print(f"✓ PDFs merged successfully!\n  Output: {output}")

            except Exception as e:
                print(f"✗ Failed to merge PDFs: {e}")

        # --------------------------------------------------
        # PDF → Image
        # --------------------------------------------------
        elif operation == "PDF → Image":
            print("\nPDF → Image")

            file = askopenfilename(
                title="Select a PDF",
                filetypes=[("PDF files", "*.pdf")],
            )

            if not file:
                print("No file selected.")
                continue

            while True:
                page_number = questionary.text(
                    "Enter page number:"
                ).ask()

                if page_number is None:
                    break

                try:
                    page_number = int(page_number)

                    if page_number < 1:
                        raise ValueError

                    break

                except ValueError:
                    print("✗ Please enter a valid page number.")

            if page_number is None:
                continue

            output = asksaveasfilename(
                title="Save image",
                defaultextension=".png",
                filetypes=[
                    ("PNG files", "*.png"),
                    ("JPEG files", "*.jpg"),
                ],
            )

            if not output:
                print("Output location not selected.")
                continue

            try:
                to_png(file, page_number, output)
                print(f"✓ Image created successfully!\n  Output: {output}")

            except Exception as e:
                print(f"✗ Failed to convert PDF: {e}")

        # --------------------------------------------------
        # Split PDF
        # --------------------------------------------------
        elif operation == "Split PDF":
            print("\nSplit PDF")

            file = askopenfilename(
                title="Select a PDF",
                filetypes=[("PDF files", "*.pdf")],
            )

            if not file:
                print("No file selected.")
                continue

            output_folder = askdirectory(
                title="Select output folder"
            )

            if not output_folder:
                print("Output folder not selected.")
                continue

            output_prefix = questionary.text(
                "Enter an output prefix:"
            ).ask()

            if output_prefix is None or not output_prefix.strip():
                print("Invalid output prefix.")
                continue

            output = path.join(output_folder, output_prefix)

            try:
                split_pdf(file, output)
                print(
                    f"✓ PDF split successfully!\n"
                    f"  Output folder: {output_folder}"
                )

            except Exception as e:
                print(f"✗ Failed to split PDF: {e}")

        # --------------------------------------------------
        # Extract Pages
        # --------------------------------------------------
        elif operation == "Extract Pages":
            print("\nExtract Pages")

            file = askopenfilename(
                title="Select a PDF",
                filetypes=[("PDF files", "*.pdf")],
            )

            if not file:
                print("No file selected.")
                continue

            page_string = questionary.text(
                "Enter page string (e.g. 1-5 or 1,3,5-8):"
            ).ask()

            if page_string is None or not page_string.strip():
                print("No pages specified.")
                continue

            output = asksaveasfilename(
                title="Save extracted PDF",
                defaultextension=".pdf",
                filetypes=[("PDF files", "*.pdf")],
            )

            if not output:
                print("Output location not selected.")
                continue

            try:
                extract_pages(file, page_string, output)
                print(
                    f"✓ Pages extracted successfully!\n"
                    f"  Output: {output}"
                )

            except Exception as e:
                print(f"✗ Failed to extract pages: {e}")


if __name__ == "__main__":
    main()
