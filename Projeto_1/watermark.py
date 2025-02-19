import numpy as np
import cv2


class Watermark:
    def __init__(self, imgs_list):
        self.watermark_path = "./watermark.png"
        self.alpha = 0.25
        self.border_const = 20
        self.imgs_list = imgs_list

    def build_watermark(self):
        img = cv2.imread("./assets/watermark.png", cv2.IMREAD_UNCHANGED)
        wm_images = []
        dim = (200, 40)

        # resize image
        resized = cv2.resize(img, dim, fx=10, fy=10, interpolation=cv2.INTER_AREA)
        cv2.imwrite('watermark.png', resized)

        watermark = cv2.imread(self.watermark_path, cv2.IMREAD_UNCHANGED)
        (wH, wW) = watermark.shape[:2]

        (B, G, R, A) = cv2.split(watermark)
        B = cv2.bitwise_and(B, B, mask=A)
        G = cv2.bitwise_and(G, G, mask=A)
        R = cv2.bitwise_and(R, R, mask=A)
        watermark = cv2.merge([B, G, R, A])
        distancia = 30

        for image in self.imgs_list:
            (h, w) = image.shape[:2]
            image = np.dstack([image, np.ones((h, w), dtype="uint8") * 255])

            overlay = np.zeros((h, w, 4), dtype="uint8")

            watermark_h, watermark_w, watermark_c = watermark.shape
            for i in range(0, watermark_h):
                for j in range(0, watermark_w):
                    if watermark[i,j][3] != 0:
                        offset = 290
                        h_offset = h - watermark_h - offset
                        w_offset = w - watermark_w - offset
                        overlay[w_offset + j, h_offset + i] = watermark[i,j]

            #overlay[h - wH - 100:h - 100, w - wW - 100:w - 100] = watermark
            #overlay[distancia:wH + distancia, distancia:wW + distancia] = watermark
            #overlay[h - 40:h, w - 200:w] = watermark

            # blend the two images together using transparent overlays
            output = image.copy()
            cv2.addWeighted(overlay, self.alpha, output, 1.0, 0, output)
            #cv2.putText(img, "center", (cX - 20, cY - 20),

            wm_images.append(output)
        return wm_images
