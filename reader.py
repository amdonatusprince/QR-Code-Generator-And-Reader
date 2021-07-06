import cv2 as cv

# read the QRCODE image
img = cv.imread("amdonatusprince-qr-code.png")

# initialize the cv2 QRCode detector
detector = cv.QRCodeDetector()

# detect and decode
data, bbox, straight_qrcode = detector.detectAndDecode(img)
print("QRCode data:", data)
