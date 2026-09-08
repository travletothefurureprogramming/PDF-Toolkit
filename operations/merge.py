import pymupdf


def merge_files(files, output="merged.pdf"):
    merger = pymupdf.open()

    for path in files:
        pdf = pymupdf.open(path)
        merger.insert_pdf(pdf)
        pdf.close()

    merger.save(output)
    merger.close()