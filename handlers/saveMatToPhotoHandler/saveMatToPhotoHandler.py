from handlers.BaseCommandHandler import BaseCommandHandler

from loaderData.loadPhoto import LoadPhoto

import cv2

import numpy as np

from processingData.cutBackground import CutBackground

class SaveMatToPhotoHandler(BaseCommandHandler):
    def __init__(self):
        pass

    def execute(self,parameters):
        # Сохранение матриц в картинки
        if parameters.pl_filter == 1:
            i = 0
            if (parameters.objectParameter.pl_mat73 == 0):
                sizeMat = parameters.objectParameter.sizeMat[0][0][0]
                N = parameters.objectParameter.N[0][0]
                N_test = parameters.objectParameter.N_test[0][0]
            else:
                sizeMat = int(parameters.objectParameter.sizeMat[0])
                N = int(parameters.objectParameter.N)
                N_test = int(parameters.objectParameter.N_test)

            ii=0
            for j in range(N_test):
                # image = np.zeros((parameters.objectParameter.sizeMat[0][0][0],  parameters.objectParameter.sizeMat[0][0][0]))
                for i in range(parameters.objectParameter.x_test1.shape[1]):
                    image = parameters.objectParameter.x_test1[j, i, :, :].astype('uint8')

                    CutBackground.thresholdMethod(image, ii, parameters.path_file_save)
                    ii+=1
                    # Сохранение в матрицы

        else:
            g=0
        return image

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
