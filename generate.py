import pyqrcode
from PIL import Image


web_address = "http://github.com/amdonatusprince"
url = pyqrcode.create(web_address)

qr_image = "amdonatusprince-qr-code.png"
url.png(qr_image, scale=10)

# opening qr_image
image = Image.open(qr_image)
image.show()
