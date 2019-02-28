from src.Photo import Photo
import random
from src.Relationship import get_relationship

def run(photos):
    max_diff = 4
    limit = 1000
    # Sort and filter
    photos = [x for x in photos if x.isHorizontal]
    photos = sorted(photos, key=lambda x: len(x.tags), reverse=True)

    print("Filtered size: " + str(len(photos)))

    starting_item = photos[0]

    photos.remove(starting_item)
    slideshow = [starting_item]

    print()
    while len(photos) > 0:
        max_score = -1
        best_img = None
        for i in range(len(photos)):
            #if abs(len(photos[i].tags) - len(slideshow[-1].tags) > max_diff) or i > limit:
            if i > limit:
                #print("current photo len",len(photos[i].tags))
                #print("last slide len",len(slideshow[-1].tags))
                #print("exit")
                break
            score = get_relationship(slideshow[-1].tags, photos[i].tags)
            if score > max_score:
                best_img = photos[i]
                max_score = score
        if best_img is not None:
            slideshow.append(best_img)
            photos.remove(best_img)
        else:
            break
        print("\rPhotos left: "+str(len(photos)) + "          ", end="")
    print("\nDone")

    return slideshow
