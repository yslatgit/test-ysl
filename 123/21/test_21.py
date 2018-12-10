data = [
 # 其他数据
 (2016, 3, 30.9, 31.9, 29.9),
 (2016, 4, 30.5, 32.5, 28.5),
 # Add more data here
 ]

from reportlab.graphics.shapes import Drawing,String
from reportlab.graphics import renderPDF

d = Drawing(100,100)
s = String(50,50,'Hello world!',textAnchor='middle')
d.add(s)
renderPDF.drawToFile(d,'hello.pdf','A simple PDF file')