"""
Класс-контроллер для работы с фотографиями (искусственными или настоящими), направленный на обработку
фотографий для итогового снижения ошибок работы нейросетей для классификации
"""


from handlers.BaseCommandHandler import BaseCommandHandler
from handlers.loadPhotosHandler.loadPhotosHandler import LoadPhotosHandler
from handlers.findContoursHandler.findContoursHandler import FindContoursHandler

class MainCommandHandler(BaseCommandHandler):
    def __init__(self):

        self.dict={}
        self.dict[0] = LoadPhotosHandler()
        self.dict[1] = FindContoursHandler()

    def initFunction(self,code_request, parameter):
        result = None
        if code_request in self.dict:
            handler = self.dict[code_request]
            result = handler.execute(parameter)

        return result