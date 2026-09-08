import questionary
from os import path
from operations.extract import extract_pages
from operations.split import split_pdf
from operations.merge import merge_files
from operations.convert import to_png
from tkinter.filedialog import askopenfilenames, asksaveasfilename, askopenfilename, askdirectory

def main():
    print("╭──────────────────────────────────╮\n" \
          "|           PDF Toolkit            |\n"
          "╰──────────────────────────────────╯\n")
    while True:


        operation = questionary.select("",choices=["Merge PDFs","PDF → Image","Split PDF","Extract Pages","Exit"]).ask()

        if operation == "Exit":
            exit()

        elif operation == "Merge PDFs":
            print("Merge PDFs")
            files = askopenfilenames()
            output = asksaveasfilename(defaultextension=".pdf",filetypes=[("PDF files", "*.pdf")])
            merge_files(files, output)

        elif operation == "PDF → Image":
            print("PDF → Image")

            file = askopenfilename()

            page_number = questionary.text("Enter page number: ").ask()

            output = asksaveasfilename(defaultextension=".png",filetypes=[("PNG files", "*.png")])
            to_png(file, int(page_number), output)

        elif operation == "Split PDF":
            print("Split PDF")

            file = askopenfilename()

            output_folder = askdirectory()

            output = questionary.text("Enter an output prefix: ").ask()

            output = path.join(output_folder, output)
            split_pdf(file, output)

        elif operation == "Extract Pages":
            print("Extract Pages")

            file = askopenfilename()
            page_string = questionary.text("Enter page string (For example 1-5) : ").ask()
            output = asksaveasfilename(defaultextension=".png",filetypes=[("PDF files", "*.pdf")])

            extract_pages(file, page_string, output)
 
        

            
if __name__ == "__main__":
    main()