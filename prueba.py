# Import essential libraries
import requests
import cv2
import numpy as np
import imutils
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

url = "http://192.168.31.95:8080/shot.jpg"

val = input("Ingrese una palabra a buscar: ")

# While loop to continuously fetching data from the Url

while True:

    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)
    img = imutils.resize(img, width=1000, height=1800)

    # Detecting Words
    altImg, anchoImg, _ = img.shape
    boxes = pytesseract.image_to_data(img)

    for x, b in enumerate(boxes.splitlines()):
        if x != 0:
            b = b.split()
            if len(b) == 12:
                if b[11] == val: # Encuentra la palabra ingresada
                    x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                    cv2.rectangle(img, (x, y), (w + x, h + y), (0, 0, 255), 3)
                    cv2.putText(img, b[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)

                    cv2.imshow("Android_cam", img)

    # Press Esc key to exit
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
