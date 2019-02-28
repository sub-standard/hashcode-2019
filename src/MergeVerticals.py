from src.Slide import Slide

def merge_verticals(photos):
    slides = []

    slides = [Slide(x) for x in photos if x.isHorizontal]

    verticals = [x for x in photos if not x.isHorizontal]

    #

    return slides
