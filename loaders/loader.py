import abc


class Loader:
    def __init__(self):
        pass

    @abc.abstractmethod
    def load_data_capsule_list(self, data_capsule_list):
        pass
