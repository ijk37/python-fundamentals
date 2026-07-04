# 07-05: Working with PDF Files

PDFs are everywhere — reports, invoices, research papers. Python can read text from them, merge/split files, and even create new ones.

```bash
pip install pypdf          # modern PDF reading/manipulation (successor to PyPDF2)
pip install reportlab      # creating PDFs from scratch
pip install pdfplumber     # better text extraction (handles tables)
pip install pymupdf        # (fitz) — fast, powerful, handles images
```

---

## Reading PDF Text with pypdf

```python
from pypdf import PdfReader

# Open a PDF
reader = PdfReader("document.pdf")

# Basic info
print(f"Pages: {len(reader.pages)}")
print(f"Encrypted: {reader.is_encrypted}")

# Metadata
meta = reader.metadata
print(f"Title:   {meta.title}")
print(f"Author:  {meta.author}")
print(f"Creator: {meta.creator}")

# Extract text from a page
page = reader.pages[0]       # first page (0-indexed)
text = page.extract_text()
print(text)

# Extract text from all pages
full_text = ""
for page in reader.pages:
    full_text += page.extract_text() + "\n"

print(full_text[:500])   # first 500 chars
```

---

## Extracting Text Page by Page

```python
from pypdf import PdfReader

def extract_pdf_text(path):
    """Extract text from all pages, return as list of strings."""
    reader = PdfReader(path)
    pages_text = []
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            pages_text.append(text.strip())
        print(f"Extracted page {i+1}/{len(reader.pages)}")
    return pages_text

pages = extract_pdf_text("report.pdf")
for i, text in enumerate(pages, 1):
    print(f"--- Page {i} ---")
    print(text[:200])
    print()
```

---

## Merging PDFs

```python
from pypdf import PdfWriter, PdfReader

def merge_pdfs(input_files, output_file):
    """Merge multiple PDFs into one."""
    writer = PdfWriter()

    for path in input_files:
        reader = PdfReader(path)
        for page in reader.pages:
            writer.add_page(page)

    with open(output_file, "wb") as f:
        writer.write(f)

    print(f"Merged {len(input_files)} files into {output_file}")

merge_pdfs(
    ["chapter1.pdf", "chapter2.pdf", "chapter3.pdf"],
    "full_book.pdf"
)
```

---

## Splitting a PDF

```python
from pypdf import PdfWriter, PdfReader

def split_pdf(input_file, pages_per_chunk, output_prefix="chunk"):
    """Split a PDF into chunks of N pages."""
    reader = PdfReader(input_file)
    total = len(reader.pages)
    chunk_num = 0

    for start in range(0, total, pages_per_chunk):
        writer = PdfWriter()
        end = min(start + pages_per_chunk, total)
        for i in range(start, end):
            writer.add_page(reader.pages[i])
        out_path = f"{output_prefix}_{chunk_num+1}.pdf"
        with open(out_path, "wb") as f:
            writer.write(f)
        print(f"Created {out_path} (pages {start+1}-{end})")
        chunk_num += 1

split_pdf("large_report.pdf", pages_per_chunk=10)
```

### Extract specific pages

```python
from pypdf import PdfWriter, PdfReader

def extract_pages(input_file, page_numbers, output_file):
    """Extract specific pages (0-indexed) into a new PDF."""
    reader = PdfReader(input_file)
    writer = PdfWriter()

    for n in page_numbers:
        writer.add_page(reader.pages[n])

    with open(output_file, "wb") as f:
        writer.write(f)

# Extract pages 0, 2, 4 (1st, 3rd, 5th)
extract_pages("document.pdf", [0, 2, 4], "selected.pdf")
```

---

## Rotating Pages

```python
from pypdf import PdfWriter, PdfReader

reader = PdfReader("sideways.pdf")
writer = PdfWriter()

for page in reader.pages:
    page.rotate(90)    # 90, 180, or 270 degrees clockwise
    writer.add_page(page)

with open("rotated.pdf", "wb") as f:
    writer.write(f)
```

---

## Adding Watermark

```python
from pypdf import PdfWriter, PdfReader

def add_watermark(input_pdf, watermark_pdf, output_pdf):
    """Overlay watermark on every page."""
    reader    = PdfReader(input_pdf)
    watermark = PdfReader(watermark_pdf).pages[0]
    writer    = PdfWriter()

    for page in reader.pages:
        page.merge_page(watermark)    # merge watermark on top
        writer.add_page(page)

    with open(output_pdf, "wb") as f:
        writer.write(f)

add_watermark("original.pdf", "watermark.pdf", "watermarked.pdf")
```

---

## Encrypting and Decrypting

```python
from pypdf import PdfWriter, PdfReader

# Encrypt a PDF
def encrypt_pdf(input_file, output_file, password):
    reader = PdfReader(input_file)
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    writer.encrypt(password)
    with open(output_file, "wb") as f:
        writer.write(f)

encrypt_pdf("document.pdf", "secure.pdf", "MySecret123")

# Decrypt / read a protected PDF
def read_protected(path, password):
    reader = PdfReader(path)
    if reader.is_encrypted:
        success = reader.decrypt(password)
        if not success:
            raise ValueError("Wrong password")
    return "\n".join(p.extract_text() for p in reader.pages)

text = read_protected("secure.pdf", "MySecret123")
print(text[:200])
```

---

## Better Text Extraction with pdfplumber

`pdfplumber` is better at preserving layout and extracting tables:

```python
import pdfplumber

# Basic text extraction
with pdfplumber.open("document.pdf") as pdf:
    for i, page in enumerate(pdf.pages):
        text = page.extract_text()
        print(f"--- Page {i+1} ---")
        print(text)

# Extract tables
with pdfplumber.open("report_with_tables.pdf") as pdf:
    page = pdf.pages[0]
    tables = page.extract_tables()
    for table in tables:
        for row in table:
            print(row)   # list of strings

# Crop a region of the page
with pdfplumber.open("document.pdf") as pdf:
    page = pdf.pages[0]
    # Crop (x0, top, x1, bottom) in points
    region = page.crop((50, 100, 400, 300))
    print(region.extract_text())
```

---

## Creating PDFs with reportlab

```python
from reportlab.lib.pagesizes import A4, letter
from reportlab.lib.units import cm, inch
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet

# Simple canvas approach
def create_simple_pdf(filename):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    # Title
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(width/2, height - 100, "Student Report")

    # Subtitle
    c.setFont("Helvetica", 14)
    c.setFillColor(colors.gray)
    c.drawCentredString(width/2, height - 130, "Academic Year 2024")

    # Line
    c.setStrokeColor(colors.black)
    c.line(50, height - 150, width - 50, height - 150)

    # Content
    c.setFont("Helvetica", 12)
    c.setFillColor(colors.black)
    y = height - 200

    students = [("Alice", 88.5, "A"), ("Bob", 92.0, "A"), ("Charlie", 79.3, "C")]
    for name, score, grade in students:
        c.drawString(100, y, f"{name}")
        c.drawString(250, y, f"Score: {score:.1f}")
        c.drawString(380, y, f"Grade: {grade}")
        y -= 25

    # Page number
    c.setFont("Helvetica", 10)
    c.drawRightString(width - 50, 30, "Page 1")

    c.save()

create_simple_pdf("report.pdf")
```

### High-level document with Platypus

```python
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def create_report(filename):
    doc = SimpleDocTemplate(filename, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    # Title
    story.append(Paragraph("Student Performance Report", styles["Title"]))
    story.append(Spacer(1, 20))

    # Body text
    story.append(Paragraph(
        "This report summarizes student performance for the current semester.",
        styles["BodyText"]
    ))
    story.append(Spacer(1, 10))

    # Table
    table_data = [
        ["Name", "Score", "Grade"],
        ["Alice",   "88.5", "A"],
        ["Bob",     "92.0", "A"],
        ["Charlie", "79.3", "C"],
    ]
    t = Table(table_data, colWidths=[200, 100, 100])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.blue),
        ("TEXTCOLOR",  (0, 0), (-1, 0), colors.white),
        ("FONTNAME",   (0, 0), (-1, 0), "Helvetica-Bold"),
        ("ALIGN",      (0, 0), (-1, -1), "CENTER"),
        ("GRID",       (0, 0), (-1, -1), 0.5, colors.grey),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.lightgrey]),
    ]))
    story.append(t)

    doc.build(story)

create_report("styled_report.pdf")
```

---

## Quick Summary

| Task | Library | Code |
|------|---------|------|
| Read text from PDF | `pypdf` | `PdfReader` + `page.extract_text()` |
| Better text/tables | `pdfplumber` | `pdfplumber.open()` |
| Merge PDFs | `pypdf` | `PdfWriter` + `add_page()` |
| Split PDF | `pypdf` | `PdfWriter` per chunk |
| Rotate pages | `pypdf` | `page.rotate(90)` |
| Watermark | `pypdf` | `page.merge_page()` |
| Encrypt | `pypdf` | `writer.encrypt(password)` |
| Create PDF | `reportlab` | `canvas.Canvas()` or `SimpleDocTemplate` |

---

> **Exercises:** [07-05: Exercises — PDF Files](../02-exercises/07-05-pdf-files-exe.md)

---

⬅️ Previous: [07-04: Working with Excel Files](07-04-excel-files.md)
➡️ Next: [07-06: pathlib and File System Operations](07-06-pathlib-and-filesystem.md)
