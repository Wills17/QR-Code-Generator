# import library to use
import qrcode as qr

# an example
data = "https://www.google.com/"

# output file name
qr_filename = "google_qr.png"

# generate qr code
site_qr_img = qr.make(data)

# save img to a file
site_qr_img.save(qr_filename)