
class Slide():
    def __init__(self, photoOne, photoTwo = None):
        self.photoOne = photoOne
        self.photoTwo = photoTwo
        self.tags = self.photoOne.tags
        if (self.photoTwo is not None):
            self.tags = self.tags.union(self.photoTwo.tags)