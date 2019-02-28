#!/bin/env python3

from src.Importer import Importer

importer = Importer("inputs/a_example.txt")

photos = importer.importDataSet()

for photo in photos:
    print(photo)
