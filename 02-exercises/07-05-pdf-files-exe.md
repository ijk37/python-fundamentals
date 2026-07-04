# 07-05: Exercises — PDF Files

> **Notes reference:** [07-05: Working with PDF Files](../01-notes/07-05-pdf-files.md)

---

## Q1: Read PDF metadata and page count
Open a PDF and print its metadata (title, author) and total page count.

**Solution**
```python
from pypdf import PdfReader

reader = PdfReader("document.pdf")   # replace with an actual PDF on your system

print(f"Pages: {len(reader.pages)}")
print(f"Encrypted: {reader.is_encrypted}")

meta = reader.metadata
print(f"Title:  {meta.title}")
print(f"Author: {meta.author}")
```

---

## Q2: Extract text from a page
Extract and print the text from the first page of a PDF.

**Solution**
```python
from pypdf import PdfReader

reader = PdfReader("document.pdf")
page   = reader.pages[0]
text   = page.extract_text()
print(text[:500])   # first 500 characters
```

---

## Q3: Extract text from all pages
Extract text from every page and collect it into a list.

**Solution**
```python
from pypdf import PdfReader

def extract_all_text(path):
    reader = PdfReader(path)
    pages  = []
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            pages.append(text.strip())
        print(f"Processed page {i+1}/{len(reader.pages)}")
    return pages

pages = extract_all_text("document.pdf")
for i, text in enumerate(pages, 1):
    print(f"--- Page {i} ---")
    print(text[:200])
```

---

## Q4: Merge PDFs
Merge `part1.pdf` and `part2.pdf` into `combined.pdf`.

**Solution**
```python
from pypdf import PdfWriter, PdfReader

def merge_pdfs(input_files, output_file):
    writer = PdfWriter()
    for path in input_files:
        reader = PdfReader(path)
        for page in reader.pages:
            writer.add_page(page)
    with open(output_file, "wb") as f:
        writer.write(f)
    print(f"Merged into {output_file}")

merge_pdfs(["part1.pdf", "part2.pdf"], "combined.pdf")
```

---

## Q5: Split a PDF into single-page files
Split `combined.pdf` into individual pages saved as `page_1.pdf`, `page_2.pdf`, etc.

**Solution**
```python
from pypdf import PdfWriter, PdfReader

def split_to_pages(input_file):
    reader = PdfReader(input_file)
    for i, page in enumerate(reader.pages):
        writer = PdfWriter()
        writer.add_page(page)
        out_path = f"page_{i+1}.pdf"
        with open(out_path, "wb") as f:
            writer.write(f)
        print(f"Saved {out_path}")

split_to_pages("combined.pdf")
```

---

## Q6: Extract specific pages
Extract pages 1 and 3 (0-indexed: 0 and 2) from a PDF.

**Solution**
```python
from pypdf import PdfWriter, PdfReader

def extract_pages(input_file, page_numbers, output_file):
    reader = PdfReader(input_file)
    writer = PdfWriter()
    for n in page_numbers:
        writer.add_page(reader.pages[n])
    with open(output_file, "wb") as f:
        writer.write(f)
    print(f"Extracted pages {page_numbers} → {output_file}")

extract_pages("document.pdf", [0, 2], "selected_pages.pdf")
```

---

## Q7: Rotate pages
Rotate all pages of a PDF by 90 degrees clockwise and save.

**Solution**
```python
from pypdf import PdfWriter, PdfReader

reader = PdfReader("document.pdf")
writer = PdfWriter()

for page in reader.pages:
    page.rotate(90)
    writer.add_page(page)

with open("rotated.pdf", "wb") as f:
    writer.write(f)
print("Rotated PDF saved.")
```

---

## Q8: Create a simple PDF with reportlab
Create a PDF report listing Bangladeshi cities and their populations.

**Solution**
```python
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def create_city_report(filename):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(width / 2, height - 80, "Bangladesh City Population Report")

    c.setFont("Helvetica", 12)
    y = height - 130

    cities = [
        ("Dhaka",      21_006_000),
        ("Chittagong",  4_009_423),
        ("Sylhet",      3_482_000),
        ("Rajshahi",    2_400_000),
        ("Khulna",      2_100_000),
    ]

    c.setFont("Helvetica-Bold", 11)
    c.drawString(80, y, "City")
    c.drawString(280, y, "Population")
    y -= 20
    c.line(80, y, 430, y)
    y -= 15

    c.setFont("Helvetica", 11)
    for city, pop in cities:
        c.drawString(80, y, city)
        c.drawString(280, y, f"{pop:,}")
        y -= 20

    c.save()
    print(f"Created {filename}")

create_city_report("city_report.pdf")
```

---

⬅️ Previous: [07-04: Exercises — Excel Files](07-04-excel-files-exe.md)
➡️ Next: [07-06: Exercises — pathlib and File System Operations](07-06-pathlib-and-filesystem-exe.md)
