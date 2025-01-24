# import library to use
import qrcode as qr
import numpy as np


# an example to be encoded
data1 = "https://www.google.com/"

# output file name
qr_filename = "qr_image1.png"

# generate qr code
img1 = qr.make(data1)

# display code encoded
img1.show(img1)

# save img to a file
img1.save(qr_filename)



"""Example 2 with bounding box"""
# new data to be encoded
data2 = "https://www.github.com/"

# create new QRCode object
qrcode = qr.QRCode(version=1, box_size=10, border=4)

# add data to the QR code
qrcode.add_data(data2)

# compile the data into a QR code array
qrcode.make()

# print the image shape
print("The shape of the QR Code image is:", np.array(qrcode.get_matrix()).shape)

# transfer the array into an actual image
img2 = qrcode.make_image(fill_color="black", back_color="white")

# display new code encoded
img2.show(img2)

# save img to file
img2.save("qr_image2.png")

