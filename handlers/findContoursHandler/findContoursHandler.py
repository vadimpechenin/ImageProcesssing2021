from handlers.BaseCommandHandler import BaseCommandHandler

from loaderData.loadPhoto import LoadPhoto

from objectStructure.objectStructure import ObjectParameter

import cv2

import numpy as np

class FindContoursHandler(BaseCommandHandler):
    def __init__(self):
        pass

    def execute(self,parameters):
        # Получение матриц фотографий и меток к ним
        #Загрузка матриц (с преобразованием их в серый цвет и изменением под нужный размер

        # параметры цветового фильтра
        # Load image, grayscale, bilaterial filter, Otsu's threshold
        for image in parameters.objectParameter.X:
            original = image.copy()
            #t = int(round(np.mean(original),0))
            blur = cv2.bilateralFilter(original, 9, int(round(np.mean(original),0))/4, int(round(np.mean(original),0))/4) #9, 75, 75
            thresh = cv2.threshold(original, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
            #thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
            #cv2.THRESH_BINARY, 11, 2)[1]

            #Выделение контура с помощью Лапласиана
            s = cv2.Laplacian(blur, cv2.CV_16S, ksize=3)
            s = cv2.convertScaleAbs(s)
            cv2.imshow('nier', s)
            # Find contours, perform contour approximation, and extract ROI
            ROI = None
            if (1==0):
                ROI_num = 0
                cnts = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                cnts = cnts[0] if len(cnts) == 2 else cnts[1]
                for c in cnts:
                    peri = cv2.arcLength(c, True)
                    approx = cv2.approxPolyDP(c, 0.04 * peri, True)
                    # If has 5 then its a pentagon
                    if len(approx) == 5:
                        x, y, w, h = cv2.boundingRect(approx)
                        cv2.rectangle(image, (x, y), (x + w, y + h), (200, 255, 12), 2)
                        ROI = original[y:y + h, x:x + w]
                        cv2.imwrite('ROI_{}.png'.format(ROI_num), ROI)
                        ROI_num += 1

            cv2.imshow('thresh', thresh)
            cv2.imshow('blur', blur)
            try:
                cv2.imshow('ROI', ROI)
            except:
                print('Нет прямоугольника для объекта')
            cv2.imshow('image', image)
            cv2.waitKey()

        return cnts
