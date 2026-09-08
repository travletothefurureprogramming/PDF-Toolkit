import pymupdf

def extarct_text(file, output="extracted_text.txt"):
    doc = pymupdf.open(file)

    with open(output,"w") as f:
        f.close()
        

    for page in doc:
        with open(output,"a") as f:
            f.write(page.get_text())

    
