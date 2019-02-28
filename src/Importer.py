import os.path

class Importer:
    def __init__(self, filename : str) -> None:
        self.filename: str = filename

    # Read the input from the input file
    def importDataSet(self):
        if os.path.isfile(self.filename):
            with open(self.filename, 'r') as file:
                return []
        else:
            print("Error: File not found")
            raise FileNotFoundError
