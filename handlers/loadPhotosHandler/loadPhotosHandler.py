from handlers.BaseCommandHandler import BaseCommandHandler

from loaderData.loadPhoto import LoadPhoto

from objectStructure.objectStructure import ObjectParameter

class LoadPhotosHandler(BaseCommandHandler):
    def __init__(self):
        pass

    def execute(self,parameters):
        # Получение матриц фотографий и меток к ним
        #Загрузка матриц (с преобразованием их в серый цвет и изменением под нужный размер

        if parameters.pl_load == 1:
            features, labels = LoadPhoto.imreadPhotoFromDir(parameters.locationFolder,
                                                            parameters.size_of_image,
                                                            numberOfClass=4)
            X, Y = LoadPhoto.returnMatrixAndSaveMat(features, labels, parameters.path_file,
                                                    parameters.name_safe_train_test)
        else:
            X, Y = LoadPhoto.loadMatrixMat(parameters.path_file,
                                                    parameters.name_safe_train_test)

        ObjectParameter.name = parameters.name_safe_train_test
        ObjectParameter.X = X
        ObjectParameter.Y = Y
        return ObjectParameter
