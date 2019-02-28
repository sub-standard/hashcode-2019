#!/bin/env python3

from src.Photo import Photo
from src.Importer import Importer
import random
from src.Relationship import get_relationship

importer = Importer("inputs/a_example.txt")
photos = importer.import_data_set()

starting_item = random.choice(photos)
while not starting_item.isHorizontal:
    starting_item = random.choice(photos)

photos.remove(starting_item)
slideshow = [starting_item]

photos = [x for x in photos if x.isHorizontal]

while len(photos) > 0:
    max_score = -1
    best_img = None
    for img in photos:
        score = get_relationship(slideshow[-1].tags, img.tags)
        if score > max_score:
            best_img = img
            max_score = score
            break
    if best_img is not None:
        slideshow.append(best_img)
        photos.remove(best_img)

print(slideshow)

f = open("out.txt", "w")
f.write(str(len(slideshow)) + "\n")
for slide in slideshow:
    f.write(str(slide.id) + "\n")
f.close()
