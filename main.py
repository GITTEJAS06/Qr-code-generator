import pyqrcode
from pyqrcode import QRCode

# String with the URL representation for the QR code
s = "https://www.ex.com/"

# Generate QR code
url = pyqrcode.create(s)

# Create and save the SVG file naming it "myqr.svg"
url.svg("myt.svg", scale=8)
