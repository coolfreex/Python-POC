from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import zipfile

# 创建一个PDF文件
pdf_file = "poc.pdf"
c = canvas.Canvas(pdf_file, pagesize=letter)
c.drawString(100, 750, "hello")
c.save()

# 创建一个ZIP文件并将PDF文件添加到ZIP中
zip_file = "poc.zip"
with zipfile.ZipFile(zip_file, 'w') as zf:
    zf.write(pdf_file, "example.pdf")

# import os
# os.remove(pdf_file)