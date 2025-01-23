#import library to use
import qrcode as qr

# an example
data = "https://www.google.com/"

# output file name
site_qr = "google_qr_code"

# generate qr code
site_qr_img = qr.make(data)

# save img to a file
site_qr_img.save(site_qr)