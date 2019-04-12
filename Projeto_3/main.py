import cv2
import numpy as np

#Eric Saboia - 140730

def ColetaNumeros(x, y, w, h, img):
    # recortando a imagem para analise
    img = img[y:y + h, x:x + w]
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # imagem em binário
    _, thresh = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY_INV)

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    lista_auxiliar = []
    for contour in contours:
        if len(contour) > 20:
            lista_auxiliar.append(contour)

    for element in lista_auxiliar:
        (x, y, w, h) = cv2.boundingRect(element)

    return len(lista_auxiliar)


im = cv2.imread("./dados.jpg", cv2.IMREAD_GRAYSCALE)
ret, thresh1 = cv2.threshold(im, 240, 255, cv2.THRESH_BINARY_INV)

detector = cv2.SimpleBlobDetector_create()

keypoints = detector.detect(thresh1)

for marker in keypoints:
    x, y = np.int(marker.pt[0]), np.int(marker.pt[1])
    pos = np.int(marker.size / 2)
    cv2.circle(im, (x, y), 3, 255, -1)
    cv2.rectangle(im, (x - pos, y - pos), (x + pos, y + pos), 0, 1)

# get contours
contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

new_list = []
for contour in contours:

    if len(contour) > 20:
        new_list.append(contour)

im = cv2.cvtColor(im, cv2.COLOR_GRAY2RGB)

for element in new_list:
    (x, y, w, h,) = cv2.boundingRect(element)
    numero = ColetaNumeros(x, y, w, h, im)

    text_x = int(x + (w / 4))
    text_y = int(y + (h / 4))
    cv2.putText(im, str(numero), (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0))

#### Demonstração dos resultados #####
cv2.imshow("Dados ", im)
cv2.waitKey(0)
