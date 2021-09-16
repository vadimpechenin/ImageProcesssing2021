#Файл основных настроек для программы

import numpy as np



class AppEnviroment:
    def __init__(self):
        self.pl_real_photo = 1 #загрузка теста реальных фотографий

        self. pl_save = 1

        self.pl_eng = 1

        self.pl_depth = 1 #Если используются проекции, то есть 112*112*3

        self.num_classes=5 # количество классов для классификации

        self.pl_save_net = 0

        self.size_of_image_for_save = (112, 112)
        self.size_of_image = (448, 448)

        self.pl_load = 0 # Загрузка фото
        self.pl_filter = 0 # Выделение контуров на фото
        self.pl_filterMat = 1

        #Пути для загрузки обучающих и тестовых данных
        self.path_file='D:\\Vadim\\Классификация_нейросети\\Matlab_подготовка_и_решение\\'
        self.path_file='D:\\Задачи в MATLAB\\ИИР\\Исследование фильтров\\Классификация_нейросети\\Matlab_подготовка_и_решение\\'
        self.name_safe1 = 'Data_for_klassification4_x_train_real_2020'
        self.name_safe2 = 'Data_for_klassification_real_2020'
        self.name_safe3 = 'Data_for_klassification_real_2020_photos'
        # Фотографии
        self.loc1 = 'photos_0704/val_0' # photos
        self.loc2 = 'photos_0704/val_3'
        self.loc3 = 'photos_0704/val_5' #'photos_0704/val_4'

        self.path_file_save = 'save_data'


        if (self.pl_depth == 1):
            self.name_safe_train_test = '/train_test_photo_112_18'
        elif (self.pl_depth == 3):
            self.name_safe_train_test = '/train_test_photo_112_3D_18'

        if (self.pl_depth == 1):
            self.nameSafeCounrotsPhoto = '/testPhoto'
        elif (self.pl_depth == 3):
            self.nameSafeCounrotsPhoto = '/testPhoto_3D'

        if (self.pl_depth == 1):
            self.nameSafeCounrotsMat = '/Traincountour'
            self.nameSafeCounrotsMatTest = '/Testcountour'
        elif (self.pl_depth == 3):
            self.nameSafeCounrotsMat = '/Traincountour_3D'
            self.nameSafeCounrotsMatTest = '/Testcountour_3D'

        # Сохранение полученных результатов оптимизации
        if self.pl_real_photo == 0:
            if (self.pl_depth == 1):
                self.name_safe_result = '/Details_result_112_VGG_2021'
            else:
                self.name_safe_result = '/Details_result_112_VGG_2021_3D'
        else:
            if (self.pl_depth == 1):
                self.name_safe_result = '/Details_result_112_VGG_2021_photo'
            else:
                self.name_safe_result = '/Details_result_112_VGG_2021_photo_3D'

        # Параметры фильтров
        ksizeLaplasian = 3 #Размер окна маски для выделения контуров, возможны нечетные варианты, идеал 3


