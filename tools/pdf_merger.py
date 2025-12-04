from PyPDF2 import PdfMerger
import glob

def merge_pdfs(output_file):
    merger = PdfMerger()

    for pdf in glob.glob("*.pdf"):
        merger.append(pdf)

    merger.write(output_file)
    merger.close()

    print(" PDFs merged")

if __name__ == "__main__":
    merge_pdfs("merged.pdf")
