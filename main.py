#!/bin/env python3

import sys
import os
from src.Photo import Photo
from src.Importer import Importer
import random
from src.Relationship import get_relationship
import zipfile

def zipdir(path):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            zipfile.ZIP_DEFLATED.write(os.path.join(root, file))

inputs = {
    "a": "a_example.txt",
    "b": "b_lovely_landscapes.txt",
    "c": "c_memorable_moments.txt",
    "d": "d_pet_pictures.txt",
    "e": "e_shiny_selfies.txt"
}

inSet = ""
inFile = ""
if sys.argv[1] in inputs.keys():
    inSet = sys.argv[1]
    inFile = "inputs/" + inputs[inSet]

importer = Importer(inFile)
photos = importer.import_data_set()

starting_item = random.choice(photos)
while not starting_item.isHorizontal:
    starting_item = random.choice(photos)

photos.remove(starting_item)
slideshow = [starting_item]

photos = [x for x in photos if x.isHorizontal]

print()
while len(photos) > 0:
    max_score = -1
    best_img = None
    for img in photos:
        score = get_relationship(slideshow[-1].tags, img.tags)
        if score > max_score:
            best_img = img
            max_score = score
    if best_img is not None:
        slideshow.append(best_img)
        photos.remove(best_img)
    else:
        break
    print("\rPhotos left: "+str(len(photos)), end="")
print("\rDone")

f = open("outputs/"+inSet+".txt", "w")
f.write(str(len(slideshow)) + "\n")
for slide in slideshow:
    f.write(str(slide.id) + "\n")
f.close()

zipdir("outputs/")


