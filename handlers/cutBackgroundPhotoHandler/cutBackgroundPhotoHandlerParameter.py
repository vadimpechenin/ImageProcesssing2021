from handlers.BaseCommandHandlerParameter import BaseCommandHandlerParameter

class CutBackgroundPhotoHandlerParameter(BaseCommandHandlerParameter):
    def __init__(self, objectParameter,pl_filter, path_file, path_file_save, name_safe_train_test, size_of_image):
        self.objectParameter = objectParameter
        self.pl_filter = pl_filter
        self.path_file = path_file
        self.path_file_save = path_file_save
        self.name_safe_train_test = name_safe_train_test
        self.size_of_image = size_of_image


