import abc


class Transformer:
    def __init__(self):
        pass

    @abc.abstractmethod
    def convert_data_raw_to_data_capsule(self, raw_data_list):
        pass

    @abc.abstractmethod
    def enrich_process(self, data_capsule_list):
        pass

    def pipeline(self, raw_data_list):
        data_capsule_list = self.convert_data_raw_to_data_capsule(raw_data_list)
        data_capsule_list = self.enrich_process(data_capsule_list)

        return data_capsule_list
