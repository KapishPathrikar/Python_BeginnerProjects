import pypdf
import os
from tkinter import Tk, filedialog, simpledialog

root = Tk()
root.withdraw()

choice = simpledialog.askinteger(
    "PDF Tool",
    "Choose Action:\n\n1 → Merge PDFs\n2 → Slice PDF",
    minvalue=1,
    maxvalue=2
)

if choice is None:
    exit()

# for merging choice 1
if choice == 1:

    pdf_files = filedialog.askopenfilenames(
        title="Select PDFs to Merge",
        filetypes=[("PDF Files", "*.pdf")]
    )

    if not pdf_files:
        print("No PDFs selected!")
        exit()

    merger = pypdf.PdfWriter()

    for pdf in pdf_files:
        reader = pypdf.PdfReader(pdf)

        for page in reader.pages:
            merger.add_page(page)

    save_path = filedialog.asksaveasfilename(
        title="Save Merged PDF",
        defaultextension=".pdf",
        filetypes=[("PDF Files", "*.pdf")]
    )

    if save_path:
        with open(save_path, "wb") as output_file:
            merger.write(output_file)

        print("PDF merged successfully!")
        os.startfile(save_path)


#for slicing choice 2
elif choice == 2:

    pdf_path = filedialog.askopenfilename(
        title="Select PDF to Slice",
        filetypes=[("PDF Files", "*.pdf")]
    )

    if not pdf_path:
        print("No PDF selected!")
        exit()

    reader = pypdf.PdfReader(pdf_path)
    writer = pypdf.PdfWriter()

    total_pages = len(reader.pages)

    # Ask page range
    page_range = simpledialog.askstring(
        "Slice PDF",
        f"PDF has {total_pages} pages.\n\nEnter range (example: 2-5)"
    )

    if not page_range:
        exit()

    # Split range
    start_page, end_page = map(int, page_range.split("-"))

    # Add pages
    for i in range(start_page - 1, end_page):
        writer.add_page(reader.pages[i])

    # Save sliced PDF
    save_path = filedialog.asksaveasfilename(
        title="Save Sliced PDF",
        defaultextension=".pdf",
        filetypes=[("PDF Files", "*.pdf")]
    )

    if save_path:
        with open(save_path, "wb") as output_file:
            writer.write(output_file)

        print("PDF sliced successfully!")
        os.startfile(save_path)