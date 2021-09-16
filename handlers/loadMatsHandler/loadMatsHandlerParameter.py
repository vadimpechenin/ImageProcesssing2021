from handlers.BaseCommandHandlerParameter import BaseCommandHandlerParameter

class LoadMatsHandlerParameter(BaseCommandHandlerParameter):
    def __init__(self, name_safe1, name_safe2, path_file, pl_save):
        self.name_safe1 = name_safe1
        self.name_safe2 = name_safe2
        self.path_file = path_file
        self.pl_save = pl_save

