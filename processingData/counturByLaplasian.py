import numpy as np
import cv2

class CounturByLaplasian:
    #Класс получения контуров с помощью билатерального фильтра и Лапласиана
    @staticmethod
    def bilateralLaplasianMethod(image, ksize):
        # Билатеральная фильтрация перед обработкой (убираем шумы)
        blur = cv2.bilateralFilter(image, 9, int(round(np.mean(image), 0)) / 4,
                                   int(round(np.mean(image), 0)) / 4)  # 9, 75, 75
        # Ранговая фильтрация (медианный фильтр) (отметаем, будем использовать в статье при сравнении)
        # medianBlur = cv2.medianBlur(original, 3)
        # Делаем черно-белый оттенок
        # thresh = cv2.threshold(original, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        # Выделение контура с помощью Лапласиана
        imageBeforeLaplacian = cv2.Laplacian(blur, cv2.CV_16S, ksize=3)
        imageBeforeLaplacian = cv2.convertScaleAbs(imageBeforeLaplacian)
        return imageBeforeLaplacian

