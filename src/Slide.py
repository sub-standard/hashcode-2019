
class Slide():
    def __init__(self, photoOne, photoTwo = None):
        self.photoOne = photoOne
        self.photoTwo = photoTwo
        self.tags = self.photoOne.tags
        if (self.photoTwo is not None):
            self.tags = self.tags.union(self.photoTwo.tags)

    def get_output_line(self):
        if self.photoTwo != None:
            return str(self.photoOne.id) + " " + str(self.photoTwo.id)
        else:
            return str(self.photoOne.id)
