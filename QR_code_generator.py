# import library to use
import qrcode as qr
import numpy as np



# an example
data = "https://www.google.com/"

# output file name
qr_filename = "google_qr.png"

# generate qr code
qr_img = qr.make(data)

# save img to a file
qr_img.save(qr_filename)



# recall data to be encoded
data = "https://www.google.com/"

# instantiate QRCode object
qrcode = qr.QRCode(version=1, box_size=10, border=5)

# add data to the QR code
qrcode.add_data(data)

# compile the data into a QR code array
qrcode.make()

# print the image shape
print("The shape of the QR image:", np.array(qr.get_matrix()).shape)
# transfer the array into an actual image
img = qr.make_image(fill_color="white", back_color="black")
# save it to a file
img.save("site_inversed.png")