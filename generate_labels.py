import csv
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm

# === KONFIGURASI ===
input_csv = "D:/shipping_summary.csv"   # ubah sesuai lokasi CSV kamu
output_pdf = "D:/shipping_labels.pdf"   # lokasi hasil PDF
labels_across = 2   # 2 kolom
labels_down = 5     # 5 baris per halaman
label_width = 99 * mm   # kira-kira setengah kertas A4 (210mm / 2)
label_height = 56 * mm  # A4 tinggi 297mm / 5 baris

# === MULAI GENERATE ===
c = canvas.Canvas(output_pdf, pagesize=A4)
page_width, page_height = A4

# Baca data CSV
with open(input_csv, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    data = list(reader)

# Posisi awal (atas ke bawah)
x_offset = 10 * mm
y_offset = page_height - label_height - 15 * mm

col = 0
row = 0

for i, record in enumerate(data):
    # Hitung posisi label
    x = x_offset + col * label_width
    y = y_offset - row * label_height

    # Tulis teks di label
    c.setFont("Helvetica", 10)
    c.drawString(x + 5 * mm, y + label_height - 10 * mm, record["buyer_name"])
    c.drawString(x + 5 * mm, y + label_height - 18 * mm, record["buyer_address"])
    c.drawString(
        x + 5 * mm, y + label_height - 26 * mm,
        f"{record['buyer_city']}, {record['buyer_zipcode']}"
    )
    c.drawString(x + 5 * mm, y + label_height - 36 * mm, f"Resi: {record['kode_resi']}")

    # Pindah kolom/baris
    col += 1
    if col == labels_across:
        col = 0
        row += 1
    if row == labels_down:
        # Halaman baru
        c.showPage()
        row = 0
        col = 0
        y_offset = page_height - label_height - 15 * mm

# Simpan hasil PDF
c.save()

print(f"✅ File label berhasil dibuat: {output_pdf}")
