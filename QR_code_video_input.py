# import library
import cv2 as cv

# open the device's camera
cam = cv.VideoCapture(0)

# initialize the cv QRCode detector
qr_detector = cv.QRCodeDetector()

while True:
    _ , vid = cam.read()
    
    # detect and decode
    data, bounding_box, _ = qr_detector.detectAndDecode(vid)
    
    # check if there is a QRCode in the image
    if bounding_box is not None:
    
        # bounding box to know there is a QR code
        print(f"Bounding Box:\n{bounding_box}\n")
        
        # display the image with lines
        for i in range(len(bounding_box)):
            
            # draw bounding lines
            point1 = tuple(map(int, bounding_box[i][0]))
            point2 = tuple(map(int, bounding_box[(i+1) % len(bounding_box)][0]))
            
            cv.line(vid, point1, point2, color=(255, 0, 0), thickness=3)
            
        if data:
            print("[+] QR Code detected.\n Decoded data:\n", data)
 
            
    # display the result
    cv.imshow("img", vid)    
    if cv.waitKey(1) == ord("q"):
        break
cam.release()
cv.destroyAllWindows()