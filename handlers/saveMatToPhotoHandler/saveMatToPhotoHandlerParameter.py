from handlers.BaseCommandHandlerParameter import BaseCommandHandlerParameter

class SaveMatToPhotoHandlerParameter(BaseCommandHandlerParameter):
    def __init__(self, objectParameter, pl_filter, path_file, path_file_save, size_of_image):
        self.objectParameter = objectParameter
        self.pl_filter = pl_filter
        self.path_file = path_file
        self.path_file_save = path_file_save
        self.size_of_image = size_of_image


