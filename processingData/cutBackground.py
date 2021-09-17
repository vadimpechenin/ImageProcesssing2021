import numpy as np
import cv2

class CutBackground:
    #Класс получения контуров с помощью билатерального фильтра и Лапласиана
    @staticmethod
    def thresholdMethod(image, ii, path_file_save):
        # Билатеральная фильтрация перед обработкой (убираем шумы)
        blur = cv2.bilateralFilter(image, 9, int(round(np.mean(image), 0)) / 4,
                                   int(round(np.mean(image), 0)) / 4)  # 9, 75, 75

        # Делаем черно-белый оттенок
        imageBeforeThreshold = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

        i, j = np.where(imageBeforeThreshold == 0)
        #Белый цвет изображения
        image[i,j] = 255
        i, j = np.where(image == 0)
        image[i, j] = 255
        cv2.imwrite(path_file_save + '/' + str(ii+1) + '.jpg', image)
        return imageBeforeThreshold