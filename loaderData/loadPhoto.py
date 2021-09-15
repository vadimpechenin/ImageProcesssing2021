import numpy as np
import os
from tqdm import tqdm
import cv2
import scipy.io

class LoadPhoto:
    @staticmethod
    def imreadPhotoFromDir(locationOfPhoto, size_of_image, numberOfClass):
        features = []
        for i in tqdm(os.listdir(locationOfPhoto)):
            path = os.path.join(locationOfPhoto, i)
            f = cv2.imread(path)
            # Преобразование в серый цвет (1 матрица)
            gray = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
            #Изменение размера
            fr = cv2.resize(gray, size_of_image)
            features.append(fr)

        labels = []

        for i in tqdm(os.listdir(locationOfPhoto)):
            labels.append(numberOfClass)

        return features, labels

    @staticmethod
    def returnMatrixAndSaveMat(features, labels, path_file, name_safe_train_test):
        X = np.array(features)
        print(X.shape)

        Y = np.array(labels)
        print(Y.shape)

        scipy.io.savemat(path_file + name_safe_train_test + '.mat', {'Y': Y, 'X': X})
        print('Сохранены матрицы в папку ' + path_file + 'Файл ' + name_safe_train_test)
        return X, Y

    @staticmethod
    def loadMatrixMat(path_file, name_safe_train_test):
        load_mat = scipy.io.loadmat(path_file + name_safe_train_test + '.mat')
        Y = np.array(load_mat['Y'])
        X = np.array(load_mat['X'])
        print('Загружены матрицы из папки ' + path_file + 'Файл ' + name_safe_train_test)
        return X, Y