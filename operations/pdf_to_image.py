import pymupdf

def to_png(path, page_number, output=None):
    doc = pymupdf.open(path)

    page = doc[page_number - 1]

    pixmap = page.get_pixmap(dpi=150)

    saved_path = output if output else f"page_{page_number}.png"
    pixmap.save(saved_path)

    doc.close()

