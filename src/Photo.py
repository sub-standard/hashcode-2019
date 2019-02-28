

class Photo():
    def __init__(self, photoId, isHorizontal, tags):
        self.id = photoId
        self.isHorizontal = isHorizontal
        self.tags = tags

    def __str__(self):
        hv = ""
        if self.isHorizontal:
            hv = "H"
        else:
            hv = "V"

        return "" + str(self.id) + " " + hv + " " + str(self.tags)
