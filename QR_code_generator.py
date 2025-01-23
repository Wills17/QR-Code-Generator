# import library to use
import qrcode as qr
import numpy as np


# an example to be encoded
data = "https://www.google.com/"

# output file name
qr_filename = "qr_image1.png"

# generate qr code
img = qr.make(data)

# display code encoded
img.show()

# save img to a file
img.save(qr_filename)



# new data to be encoded
data = "https://www.github.com/"

# create new QRCode object
qrcode = qr.QRCode(version=1, box_size=10, border=5)

# add data to the QR code
qrcode.add_data(data)

# compile the data into a QR code array
qrcode.make()

# print the image shape
print("The shape of the QR Code image is:", np.array(qrcode.get_matrix()).shape)

# transfer the array into an actual image
img = qrcode.make_image(fill_color="black", back_color="yellow")

# save it to a file
img.save("qr_image2.png")

# display new code encoded
img.show()


"""Read QR Code"""

import cv2

# read a QRCODE image
img = cv2.imread("qr.image2.png")

# initialize QRCode detector
qr_detector = cv2.QRCodeDetector()

# detect and decode the image
data, bbox, straight_qrcode = qr_detector.detectAndDecode(img)

