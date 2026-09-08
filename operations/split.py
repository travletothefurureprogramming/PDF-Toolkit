import pymupdf


def split_pdf(path, output_prefix="page"):
    doc = pymupdf.open(path)

    for i, page in enumerate(doc):
        out = pymupdf.open()

        out.insert_pdf(
            doc,
            from_page=i,
            to_page=i
        )

        out.save(f"{output_prefix}_{i + 1}.pdf")
        out.close()

    doc.close()