import numpy as np
import os
from tqdm import tqdm
import cv2
import scipy.io


def resize2SquareKeepingAspectRation(img, size, interpolation):
    #Метод для сохраниния размерности
    h, w = img.shape[:2]
    c = None if len(img.shape) < 3 else img.shape[2]
    if h == w: return cv2.resize(img, (size, size), interpolation)
    if h > w:
        dif = h
    else:
        dif = w
    x_pos = int((dif - w) / 2.)
    y_pos = int((dif - h) / 2.)
    if c is None:
        mask = np.zeros((dif, dif), dtype=img.dtype)
        #mask = np.full((dif, dif), 255, dtype=img.dtype)
        mask[y_pos:y_pos + h, x_pos:x_pos + w] = img[:h, :w]

    else:
        mask = np.zeros((dif, dif, c), dtype=img.dtype)
        #mask = np.full((dif, dif, c), 255, dtype=img.dtype)
        mask[y_pos:y_pos + h, x_pos:x_pos + w, :] = img[:h, :w, :]
    return cv2.resize(mask, (size, size), interpolation)


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
            #fr = cv2.resize(gray, size_of_image, cv2.INTER_AREA)
            fr = resize2SquareKeepingAspectRation(gray, size_of_image[0], cv2.INTER_AREA)
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

    @staticmethod
    def saveMat(X, path_file, name_safe_train_test):
        scipy.io.savemat(path_file + name_safe_train_test + '.mat', {'X': X})
        print('Сохранены матрицы в папку ' + path_file + 'Файл ' + name_safe_train_test)

    @staticmethod
    def loadMat(path_file, name_safe_train_test):
        load_mat = scipy.io.loadmat(path_file + name_safe_train_test + '.mat')
        X = np.array(load_mat['X'])
        print('Загружены матрицы из папки ' + path_file + 'Файл ' + name_safe_train_test)
        return X

