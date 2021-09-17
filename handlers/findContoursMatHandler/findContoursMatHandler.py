from handlers.BaseCommandHandler import BaseCommandHandler

from loaderData.loadPhoto import LoadPhoto

import cv2

import numpy as np

from processingData.counturByLaplasian import CounturByLaplasian

class FindContoursMatHandler(BaseCommandHandler):
    def __init__(self):
        pass

    def execute(self,parameters):
        # Выделение контуров на матрицах
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
            XtrainContour = np.zeros((N, parameters.size_of_image[0], parameters.size_of_image[1], 3))
            XtestContour = np.zeros((N_test, parameters.size_of_image[0],
                                     parameters.size_of_image[1], 3))
            # параметры цветового фильтра
            # Load image, grayscale, bilaterial filter, Otsu's threshold
            for j in range(N):
                # image = np.zeros((parameters.objectParameter.sizeMat[0][0][0],  parameters.objectParameter.sizeMat[0][0][0]))
                for i in range(parameters.objectParameter.x_train1.shape[1]):
                    image = parameters.objectParameter.x_train1[j, i, :, :].astype('uint8')
                    imageBeforeLaplacian = CounturByLaplasian.bilateralLaplasianMethod(image, 3)

                    if (1 == 0):
                        self.plotResults(imageBeforeLaplacian, image)

                    # Сохранение в матрицы
                    XtrainContour[j, :, :, i] = cv2.resize(imageBeforeLaplacian, parameters.size_of_image).astype(
                        np.float32)

            for j in range(N_test):
                # image = np.zeros((parameters.objectParameter.sizeMat[0][0][0],  parameters.objectParameter.sizeMat[0][0][0]))
                for i in range(parameters.objectParameter.x_test1.shape[1]):
                    image = parameters.objectParameter.x_test1[j, i, :, :].astype('uint8')
                    imageBeforeLaplacian = CounturByLaplasian.bilateralLaplasianMethod(image, 3)

                    if (1 == 0):
                        self.plotResults(imageBeforeLaplacian, image)

                    # Сохранение в матрицы
                    XtestContour[j, :, :, i] = cv2.resize(imageBeforeLaplacian, parameters.size_of_image).astype(
                        np.float32)

            LoadPhoto.saveMat(XtrainContour, parameters.path_file,
                                             parameters.name_safe_train)

            LoadPhoto.saveMat(XtestContour, parameters.path_file,
                                             parameters.name_safe_test)

        else:
            XtrainContour = LoadPhoto.loadMat(parameters.path_file,
                              parameters.name_safe_train)

            XtestContour= LoadPhoto.loadMat(parameters.path_file,
                              parameters.name_safe_test)
        return XtestContour

    def plotResults(self, imageBeforeLaplacian, image):
        cv2.imshow('nier', imageBeforeLaplacian)
        cv2.imshow('image', image)
        cv2.waitKey()
