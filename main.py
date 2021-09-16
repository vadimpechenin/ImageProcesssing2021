"""
Система для экспериментальной обработки изображений (настоящих и искусственно сгенерированных)
для снижения погрешностей классификации нейронных сетей
"""

from appEnviroment.appEnviroment import AppEnviroment
from handlers.mainHandler import MainCommandHandler
from handlers.loadPhotosHandler.loadPhotosHandlerParameter import LoadPhotosHandlerParameter
from handlers.findContoursPhotoHandler.findContoursHandlerParameter import FindContoursHandlerParameter
from handlers.loadMatsHandler.loadMatsHandlerParameter import LoadMatsHandlerParameter
from handlers.findContoursMatHandler.findContoursMatHandlerParameter import FindContoursMatHandlerParameter

enviromentObject = AppEnviroment()
handlerObject = MainCommandHandler()

parameters = LoadPhotosHandlerParameter(enviromentObject.loc3, enviromentObject.path_file,
                                        enviromentObject.name_safe_train_test, enviromentObject.pl_load,
                                        enviromentObject.size_of_image)

# Загрузка картинок для дальнейшей обработки
objectParameter = handlerObject.initFunction(0, parameters)
# Обработка изображений с использованием
parameters = FindContoursHandlerParameter(objectParameter,enviromentObject.pl_filter,enviromentObject.path_file,
                                        enviromentObject.nameSafeCounrotsPhoto, enviromentObject.size_of_image_for_save)
counturs = handlerObject.initFunction(1, parameters)

#Загрузка mat файла
parameters = LoadMatsHandlerParameter(enviromentObject.name_safe1, enviromentObject.name_safe2,
                                      enviromentObject.path_file, enviromentObject.pl_save)
objectMatParameter = handlerObject.initFunction(2, parameters)
#Контура с mat файла
parameters = FindContoursMatHandlerParameter(objectMatParameter, enviromentObject.pl_filterMat, enviromentObject.path_file,
                                        enviromentObject.nameSafeCounrotsMat, enviromentObject.nameSafeCounrotsMatTest, enviromentObject.size_of_image_for_save)
countursMat = handlerObject.initFunction(3, parameters)
g = 0

