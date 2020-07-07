class DataCapsule():
    def __init__(self, version=1, document=None, processed_fields=None):
        if processed_fields is None:
            processed_fields = {}
        self.version = version

        # An object of document class
        self.document = document

        # A dictionary of processed fields
        self.processed_fields = processed_fields

    def add_processed_fields(self, processed_fields):
        self.processed_fields = {**self.processed_fields, **processed_fields}
