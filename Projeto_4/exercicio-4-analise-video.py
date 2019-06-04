import cv2
import numpy as np
import argparse
from matplotlib import pyplot as plt

def buscaFaces(self, img2, subImg):
        height, width = img2.shape[0], img2.shape[1]
        offset = 3
        maxOffset = 200
        minOffset = 30
        if height > offset+4 and width >offset+4 \
            and height < maxOffset and width < maxOffset \
            and height > minOffset and width > minOffset:
            img = img2[offset:width-offset,offset:height-offset].copy()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            _,thresh = cv2.threshold(gray, 160, 250, cv2.THRESH_BINARY_INV)

            kernel = np.ones((4, 4), np.uint8)
            thresh = cv2.dilate(thresh, kernel, iterations=1)
            thresh = cv2.erode(thresh, kernel, iterations=1)

            cv2.imshow("tresh",thresh)
            cv2.imshow("gray",gray)
            contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            circulos=0

            for contour in contours:

                approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
                cv2.drawContours(gray, [approx], 0, (0), 5)

                if len(approx)>=5:
                    circulos += 1
            return str(circulos)

def cortaRetangulo(self, img, rect):
        center, size, angle = rect[0], rect[1], rect[2]
        center, size = tuple(map(int, center)), tuple(map(int, size))
        height, width = img.shape[0], img.shape[1]
        M = cv2.getRotationMatrix2D(center, angle, 1)
        img_rot = cv2.warpAffine(img, M, (width, height))
        img_crop = cv2.getRectSubPix(img_rot, size, center)
        return img_crop, img_rot

def buscaInformacao(self, imagemInicial):

        img = cv2.cvtColor(imagemInicial.copy(), cv2.COLOR_BGR2GRAY)

        kernel = np.ones((13, 13), np.uint8)
        img = cv2.dilate(img, kernel, iterations=1)
        img = cv2.erode(img, kernel, iterations=1)

        _,thresh = cv2.threshold(img, 245, 250, cv2.THRESH_BINARY_INV)

        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:

            approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
            if len(approx) >= 6 and len(approx) <= 12 :
                (x, y, w, h) = cv2.boundingRect(contour)
                data = img[y: y + h, x: x + w]
                rect = cv2.minAreaRect(contour)
                box = cv2.boxPoints(rect)
                box = np.int0(box)
                img_crop, img_rot = cortaRetangulo(object, imagemInicial, rect)
                face = buscaFaces(object, img_crop, data)
                cv2.putText(imagemInicial, face, (x + int(w / 2), y + int(h / 2)), font, 1, (0))

        return imagemInicial


font = cv2.FONT_HERSHEY_TRIPLEX
#processamento()
print("processando")
cap = cv2.VideoCapture('Lancamento_de_dois_dados.mp4')
success,image = cap.read()
count = 0
success = True
while success:
    success, frame = cap.read()
    frame = buscaInformacao(object, frame)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
    	break

cap.release()
cv2.destroyAllWindows()