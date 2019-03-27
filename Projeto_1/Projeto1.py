import time
import cv2
import os

from Projeto_1.watermark import Watermark

images = []
fileCopy: str = ""
size = (300, 300)

cv2.waitKey()
cv2.destroyAllWindows()


def load_images_from_folder(folder):
    images_inside_function = []
    for filename in os.listdir(folder):
        image = cv2.imread(os.path.join(folder, filename))
        try:
            img: None = cv2.resize(image, size)
            pass
        except (RuntimeError, TypeError):
            print('Error image conversion!')
            exit(1)
        if img is not None:
            imgcopy = img.copy()
            # Responde a questão 3
            imgcopy = cv2.copyMakeBorder(imgcopy, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=[0, 0, 0])
            images_inside_function.append(imgcopy)
            img = None
    images_wm = Watermark(images_inside_function).build_watermark()
    transitions(images_wm)


def transitions(imported_images):
    count = 0
    while True:
        # Responde a questão 6
        if cv2.waitKey(25) & 0xFF == ord('q'):
            exit(1)
        j = 0
        while j < len(imported_images):
            if count < len(imported_images) - 1:
                for i in range(0, 11):
                    # Responde a questão 2
                    transition: None = cv2.addWeighted(imported_images[count + 1],
                                                       (i / 10.0), imported_images[count], 1 - (i / 10.0), 0)
                    cv2.imshow('I-Transition', transition)
            count += 1
            # Responde a questão 5
            if count == len(imported_images) - 1:
                count = 0
            j += 1
        # Responde a questão 1
        time.sleep(2)


if __name__ == "__main__":
    load_images_from_folder('./assets/imagens/')

