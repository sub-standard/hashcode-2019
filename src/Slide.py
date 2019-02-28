
class Slide():
    def __init__(self, photoOne, photoTwo = None):
        self.photoOne = photoOne
        self.photo = photoTwo

    def getTags(self):
        tags = self.photoOne.tags
        if(self.photoTwo is not None):
            tags = tags.union(self.photoTwo.tags)
        return tags


