"""
Класс-контроллер для работы с фотографиями (искусственными или настоящими), направленный на обработку
фотографий для итогового снижения ошибок работы нейросетей для классификации
"""


from handlers.BaseCommandHandler import BaseCommandHandler
from handlers.loadPhotosHandler.loadPhotosHandler import LoadPhotosHandler
from handlers.findContoursPhotoHandler.findContoursHandler import FindContoursHandler
from handlers.loadMatsHandler.loadMatsHandler import LoadMatsHandler
from handlers.findContoursMatHandler.findContoursMatHandler import FindContoursMatHandler
from handlers.cutBackgroundPhotoHandler.cutBackgroundPhotoHandler import CutBackgroundPhotoHandler
from handlers.saveMatToPhotoHandler.saveMatToPhotoHandler import SaveMatToPhotoHandler

class MainCommandHandler(BaseCommandHandler):
    def __init__(self):

        self.dict={}
        self.dict[0] = LoadPhotosHandler()
        self.dict[1] = FindContoursHandler()
        self.dict[2] = LoadMatsHandler()
        self.dict[3] = FindContoursMatHandler()
        self.dict[4] = CutBackgroundPhotoHandler()
        self.dict[5] = SaveMatToPhotoHandler()

    def initFunction(self,code_request, parameter):
        result = None
        if code_request in self.dict:
            handler = self.dict[code_request]
            result = handler.execute(parameter)

        return result