import pyqrcode
import png

from pyqrcode import QRCode

url = "https://www.youtube.com"

pythonUrl = pyqrcode.create(url)

pythonUrl.svg("myqr.svg", scale=8)
pythonUrl.png("myqr.png",scale=6)

