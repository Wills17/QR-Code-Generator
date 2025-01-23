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
#img.show()

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
img = qrcode.make_image(fill_color="black", back_color="white")

# display new code encoded
#img.show()

# save it to a file
img.save("qr_image2.png")




"""Read QR Code"""

import cv2 as cv

# read a QRCODE image
img = cv.imread("qr_image2.png")

if img is None:
    print("Error: Image not found!")
    exit()
    
# display original image
cv.imshow("qr_image2.png", img)

# initialize QRCode detector
qr_detector = cv.QRCodeDetector()

# detect and decode the image
data, bbox, straight_qrcode = qr_detector.detectAndDecode(img)

# bounding box to know there is a QR code
if bbox is not None:
    print(f"QRCode data:\n{data}")
    
    print(f"Bounding Box:\n{bbox}")
    
    # display the image with lines
    # length of bounding box
    n_lines = len(bbox)
    
    for i in range(n_lines):
        
        # draw all lines        
        point1 = tuple(map(int, bbox[i][0]))
        point2 = tuple(map(int, bbox[(i + 1) % n_lines][0]))  # Connect to the next point (looping back)
        
        
        cv.line(img, point1, point2, color=(255, 0, 0), thickness=2)
        
        
# display the result
cv.imshow("With bounding box", img)
cv.waitKey(0)
cv.destroyAllWindows()