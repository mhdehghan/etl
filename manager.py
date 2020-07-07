from extractors.test_extractor import *
from loaders.loader import *
from transformers.transformer import Transformer


class Manager:
    def __init__(self, extractor_type='extractor', transformer_type='transformer',
                 loader_type='loaders'):
        self.extractor_type = extractor_type
        self.transformer_type = transformer_type
        self.loader_type = loader_type

    def process(self):
        extractor = self.create_extractor()
        transformer = self.create_transformer()
        loader = self.create_loader()

        while True:
            raw_data_list = extractor.fetch_data()
            data_capsule_list = transformer.pipeline(raw_data_list)
            loader.load_data_capsule_list(data_capsule_list)


    def create_extractor(self):
        if self.extractor_type == 'extractor':
            return Extractor()
        if self.extractor_type == 'TestExtractor':
            return TestExtractor()
        #######################################################
        # Your code
        #######################################################


    def create_transformer(self):
        if self.transformer_type == 'transformer':
            return Transformer()
        #######################################################
        # Your code
        #######################################################

    def create_loader(self):
        if self.loader_type == 'loaders':
            return Loader()
        #######################################################
        # Your code
        #######################################################


if __name__ == '__main__':
    #######################################################
    # Your code including reading configs from config file!
    # Pass the config file address using arguments (Hint: You can use 'import sys' package)

    manager = Manager()
    manager.process()
    #######################################################
#######################################################################
# You should edit these classes:
# manager.py
# test_document.py
# csv_extractor.py
# test_transformer.py
# test_logger.py
# test_loader.py
#######################################################################

