import pymupdf


def parse_pages(page_string):
    pages = []

    parts = page_string.split(",")

    for part in parts:
        part = part.strip()

        if "-" in part:
            start, end = part.split("-", 1)

            start = int(start)
            end = int(end)

            if start > end:
                raise ValueError(f"Invalid page range: {part}")

            pages.extend(range(start, end + 1))

        else:
            pages.append(int(part))

    return pages


def extract_pages(path, page_string, output="extracted.pdf"):
    doc = pymupdf.open(path)
    out = pymupdf.open()

    pages = parse_pages(page_string)

    for page_number in pages:
        if page_number < 1 or page_number > len(doc):
            raise ValueError(
                f"Page {page_number} does not exist. "
                f"PDF has {len(doc)} pages."
            )

        out.insert_pdf(
            doc,
            from_page=page_number - 1,
            to_page=page_number - 1
        )

    out.save(output)

    out.close()
    doc.close()