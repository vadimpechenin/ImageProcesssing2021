from handlers.BaseCommandHandler import BaseCommandHandler

from loaderData.loadPhoto import LoadPhoto

import cv2

import numpy as np

from processingData.cutBackground import CutBackground

class CutBackgroundPhotoHandler(BaseCommandHandler):
    def __init__(self):
        pass

    def execute(self,parameters):
        # Выделение контуров на матрицах
        if parameters.pl_filter == 1:
            i = 0
            Xt = np.zeros((parameters.objectParameter.X.shape[0], parameters.size_of_image[0], parameters.size_of_image[1], 1))
            # параметры цветового фильтра
            # Load image, grayscale, bilaterial filter, Otsu's threshold
            for image in parameters.objectParameter.X:

                imageCutPhone = CutBackground.thresholdMethod(image, i, parameters.path_file_save)

                # Find contours, perform contour approximation, and extract ROI
                # Перспективная технология, пока не выделяем прямоугольник
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
                if (1==0):
                    self.plotResults(thresh, blur, medianBlur, imageBeforeLaplacian, ROI, image)

                #Сохранение в матрицы
                Xt[i, :, :, 0] = cv2.resize(imageCutPhone,parameters.size_of_image).astype(np.float32)
                i+=1
            LoadPhoto.saveMat(Xt, parameters.path_file,
                                             parameters.name_safe_train_test)

        else:
            Xt = LoadPhoto.loadMat(parameters.path_file,
                              parameters.name_safe_train_test)
        return Xt

    def plotResults(self, thresh, blur, medianBlur, imageBeforeLaplacian, ROI, image):
        cv2.imshow('thresh', thresh)
        cv2.imshow('blur', blur)
        cv2.imshow('medianBlur', medianBlur)
        cv2.imshow('nier', imageBeforeLaplacian)
        try:
            cv2.imshow('ROI', ROI)
        except:
            print('Нет прямоугольника для объекта')
        cv2.imshow('image', image)
        cv2.waitKey()
