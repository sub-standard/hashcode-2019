from src.Photo import Photo
import random
from src.Relationship import get_relationship

def run(slides):
    max_diff = 4
    limit = 1000
    # Sort and filter
    slides = sorted(slides, key=lambda x: len(x.tags), reverse=True)

    starting_item = slides[0]

    slides.remove(starting_item)
    slideshow = []
    slideshow.append(starting_item)

    print("Running slides...")
    while len(slides) > 0:
        max_score = -1
        best_img = None
        for i in range(len(slides)):
            #if abs(len(slides[i].tags) - len(slideshow[-1].tags) > max_diff) or i > limit:
            if i > limit:
                #print("current photo len",len(slides[i].tags))
                #print("last slide len",len(slideshow[-1].tags))
                #print("exit")
                break
            score = get_relationship(slideshow[-1].tags, slides[i].tags)
            if score > max_score:
                best_img = slides[i]
                max_score = score
        if best_img is not None:
            slideshow.append(best_img)
            slides.remove(best_img)
        else:
            break

        length = len(slides)
        if length % 50 == 0:
            print("\rSlides left: "+str(length) + "          ", end="")
    print("\nDone")

    return slideshow
