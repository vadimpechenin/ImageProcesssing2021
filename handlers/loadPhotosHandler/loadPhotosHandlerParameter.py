from handlers.BaseCommandHandlerParameter import BaseCommandHandlerParameter

class LoadPhotosHandlerParameter(BaseCommandHandlerParameter):
    def __init__(self, locationFolder, path_file, name_safe_train_test, pl_load, size_of_image):
        self.locationFolder = locationFolder
        self.path_file = path_file
        self.name_safe_train_test = name_safe_train_test
        self.pl_load = pl_load
        self.size_of_image = size_of_image

