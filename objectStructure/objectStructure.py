

class ObjectParameter:
    def __init__(self):
        self.name = ''
        self.X = []
        self.Y = []


class ObjectStructure:
    @staticmethod
    def clearObject(parameter):
        parameter.name = ''
        parameter.X = []
        parameter.Y = []
        return parameter