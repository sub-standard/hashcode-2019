import os.path

from src.Photo import Photo

class Importer:
    def __init__(self, filename : str) -> None:
        self.filename: str = filename

    # Read the input from the input file
    def importDataSet(self):
        if os.path.isfile(self.filename):
            with open(self.filename, 'r') as file:
                content = file.readlines()

                N = int(content[0])

                photos = []

                lines = iter(content)
                next(lines)
                counter: int = 1
                for line in lines:
                    line = line.strip()
                    parts = line.split(" ")

                    isHorizontal = (parts[0] == "H")
                    tags = set()

                    for i in range(2, len(parts)):
                        tags.add(parts[i])

                    photo = Photo(counter, isHorizontal, tags)
                    photos.append(photo)

                    counter += 1

                file.close()

                return photos
        else:
            print("Error: File not found")
            raise FileNotFoundError
