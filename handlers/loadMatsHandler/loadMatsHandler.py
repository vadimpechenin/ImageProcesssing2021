from handlers.BaseCommandHandler import BaseCommandHandler

from loaderData.loadMatFile import LoadMatFile

from objectStructure.objectStructure import ObjectMatParameter

class LoadMatsHandler(BaseCommandHandler):
    def __init__(self):
        pass

    def execute(self,parameters):
        # Получение матриц фотографий и меток к ним
        #Загрузка матриц, определенного размера и цвета
        if parameters.pl_save == 1:
            x_train1, y_train1, x_test1, y_test1, N, N_test, H, L, pl_mat73 = LoadMatFile.loadMatTrain(parameters.path_file, parameters.name_safe1, parameters.name_safe2)

            ObjectMatParameter.name = parameters.name_safe1
            ObjectMatParameter.x_train1 = x_train1
            ObjectMatParameter.y_train1 = y_train1

            ObjectMatParameter.x_test1 = x_test1
            ObjectMatParameter.y_test1 = y_test1

            ObjectMatParameter.N = N
            ObjectMatParameter.N_test = N_test
            ObjectMatParameter.sizeMat = [H, L]
            ObjectMatParameter.pl_mat73 = pl_mat73

        return ObjectMatParameter
