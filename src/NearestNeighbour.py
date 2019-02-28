import Photo
import Importer
import Random

importer = Importer("a_example")
photos = importer.importDataSet();

starting_item = Random.choice(photos);
while not starting_img_item.isHorizontal:
    starting_item = Random.choice(photos)

photos.remove(starting_item)
slideshow = [starting_item]

photos = [x for x in photos if x.isHorizontal]

while len(photos) > 0:
    max_score = -1;
    best_img = None;
    for img in photos:
        score = get_relationship(slideshow[-1].tags,img.tags)
        if score > max_score:
            best_img = img
            max_score = score
            break
    if best_img is not None:
        slideshow.append(best_img)
        photos.remove(best_img)

print(slideshow)

