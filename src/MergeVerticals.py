import sys
from src.Slide import Slide
from src.Relationship import get_relationship

def merge_verticals(photos):
    slides = []

    slides = [Slide(x) for x in photos if x.isHorizontal]
    print("Horizontal: " + str(len(slides)))

    verticals = [x for x in photos if not x.isHorizontal]
    print("Vertical: " + str(len(verticals)))

    if len(verticals) == 0:
        return slides

    limit = 1000
    # Sort and filter
    verticals = sorted(verticals, key=lambda x: len(x.tags), reverse=True)

    print("Merging verticals...")
    while len(verticals) > 0:
        currentPhoto = verticals[0]
        verticals.remove(currentPhoto)
        min_score = sys.maxsize
        best_img = None
        for i in range(len(verticals)):
            if i > limit:
                break
            j = i - len(verticals)
            score = get_relationship(currentPhoto.tags, verticals[j].tags)
            if score < min_score:
                best_img = verticals[j]
                min_score = score
        if best_img is not None:
            slides.append(Slide(currentPhoto, best_img))
            verticals.remove(best_img)
        else:
            break

        length = len(verticals)
        if length % 50 == 0:
            print("\rVerticals left: "+str(length) + "          ", end="")
    print("\nDone")

    return slides
