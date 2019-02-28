from src.Photo import Photo
import random
from src.Relationship import get_relationship

def run(photos):
    max_diff = 2
    limit = 100000
    starting_item = photos[0]

    photos.remove(starting_item)
    slideshow = [starting_item]

    print()
    while len(photos) > 0:
        max_score = -1
        best_img = None
        for i in range(len(photos)):
            if len(photos[i].tags) - len(slideshow[-i].tags) > max_diff or i > limit:
                break
            score = get_relationship(slideshow[-1].tags, img.tags)
            if score > max_score:
                best_img = img
                max_score = score
        if best_img is not None:
            slideshow.append(best_img)
            photos.remove(best_img)
        else:
            break
        print("\rPhotos left: "+str(len(photos)) + "          ", end="")
    print("\nDone")

    return slideshow
