

class ObjectParameter:
    def __init__(self):
        self.name = ''
        self.X = []
        self.Y = []

class ObjectMatParameter:
    def __init__(self):
        self.name = ''
        self.x_train1 = []
        self.y_train1 = []

        self.x_test1 = []
        self.y_test1 = []

        self.N = []
        self.N_test = []
        self.sizeMat = []

class ObjectStructure:
    @staticmethod
    def clearObject(parameter):
        parameter.name = ''
        parameter.X = []
        parameter.Y = []
        return parameter