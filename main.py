"""
Система для экспериментальной обработки изображений (настоящих и искусственно сгенерированных)
для снижения погрешностей классификации нейронных сетей
"""

from appEnviroment.appEnviroment import AppEnviroment
from handlers.mainHandler import MainCommandHandler
from handlers.loadPhotosHandler.loadPhotosHandlerParameter import LoadPhotosHandlerParameter
from handlers.findContoursHandler.findContoursHandlerParameter import FindContoursHandlerParameter

enviromentObject = AppEnviroment()
handlerObject = MainCommandHandler()

parameters = LoadPhotosHandlerParameter(enviromentObject.loc3, enviromentObject.path_file,
                                        enviromentObject.name_safe_train_test, enviromentObject.pl_load,
                                        enviromentObject.size_of_image)

# Загрузка картинок для дальнейшей обработки
objectParameter = handlerObject.initFunction(0, parameters)
# Обработка изображений с использованием
parameters = FindContoursHandlerParameter(objectParameter)
counturs = handlerObject.initFunction(1, parameters)
g = 0

