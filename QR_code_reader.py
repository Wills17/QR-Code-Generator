"""Read QR Code from file"""
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

# check if a QR code is detected
if bbox is not None:
    print(f"QRCode data:\n{data}\n")
    
    # bounding box to know there is a QR code
    print(f"Bounding Box:\n{bbox}\n")
    
    # display the image with lines
    # length of bounding box
    n_lines = len(bbox)
    
    for i in range(n_lines):
        # draw bounding lines        
        point1 = tuple(map(int, bbox[i][0]))
        point2 = tuple(map(int, bbox[(i+1) % n_lines][0]))
        
        print(f"Drawing line from {point1} to {point2}\n")  # Debug output
        cv.line(img, point1, point2, color=(0, 0, 255), thickness=3)
        
else:
    print("No QR code detected!\n")    
    
# display the result
cv.imshow("With bounding box", img)
cv.waitKey(0)
cv.destroyAllWindows()