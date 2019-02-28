#!/bin/env python3

import sys
import os
from src.Photo import Photo
from src.Importer import Importer
import random
from src.Relationship import get_relationship
import zipfile
from src.NearestNeighbour import run

def zipdir():
    # ziph is zipfile handle
    zipf = zipfile.ZipFile('outputs.zip', 'w', zipfile.ZIP_DEFLATED)

    for root, dirs, files in os.walk("src/"):
        for file in files:
            zipf.write(os.path.join(root, file))
    zipf.write("main.py")
    # for root, dirs, files in os.walk(path):
    #     for file in files:
    #         filename, file_extension = os.path.splitext(file)
    #         print(file_extension)
    #         if file_extension is ".txt" or ".py":
    #             print(root)
    #             print(file)
    #             zipf.write(os.path.join(root, file))

inputs = {
    "a": "a_example.txt",
    "b": "b_lovely_landscapes.txt",
    "c": "c_memorable_moments.txt",
    "d": "d_pet_pictures.txt",
    "e": "e_shiny_selfies.txt"
}

inSet = ""
inFile = ""
if len(sys.argv) >= 2 and sys.argv[1] in inputs.keys():
    inSet = sys.argv[1]
    inFile = "inputs/" + inputs[inSet]
else:
    print("Please specify a input set from the following:")
    for i in inputs.keys():
        print(str(i), end=" ")
    sys.exit()

importer = Importer(inFile)
photos = importer.import_data_set()

print("Initial size: " + str(len(photos)))

# Let's get started

slides = run(photos)

f = open("outputs/"+inSet+".txt", "w")
f.write(str(len(slides)) + "\n")
for slide in slides:
    f.write(str(slide.id) + "\n")
f.close()

zipdir()


