import abc


class Extractor(metaclass=abc.ABCMeta):
    def __init__(self):
        pass

    @abc.abstractmethod
    def fetch_data(self):
        pass
