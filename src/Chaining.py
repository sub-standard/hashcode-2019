from src.Photo import Photo
import random
from src.Slide import Slide
from src.Relationship import get_relationship
from copy import deepcopy


class Link():
    def __init__(self, list_of_photos):
        self.list_of_photos = list_of_photos
        self.left_photo = self.list_of_photos[0]
        self.right_photo = self.list_of_photos[-1]

    def chain_left(self, link):
        self.list_of_photos += link.list_of_photos
        self.right_photo = self.list_of_photos.pop()
        self.list_of_photos.append(self.right_photo)

    def chain_right(self, link):
        self.list_of_photos = link.list_of_photos + self.list_of_photos
        self.left_photo = self.list_of_photos.pop()
        self.list_of_photos.append(self.left_photo)


def run(photos):
    limit = 100
    # Sort and filter
    photos = sorted(photos, key=lambda x: len(x.tags), reverse=True)

    print("Filtered size: " + str(len(photos)))

    starting_item = photos[0]

    photos.remove(starting_item)
    slideshow = []
    slideshow.append(starting_item)

    links = [Link([x]) for x in photos]

    while (len(links) > 1):
        temp_links = deepcopy(links)
        new_links = []

        while len(temp_links) > 1:
            max_score = -1
            best_link = None
            left_chain = False
            current_link = temp_links[0]  # find best match for this
            temp_links.remove(current_link)
            for i in range(len(temp_links)):
                if i > limit:
                    break

                left = get_relationship(
                    current_link.right_photo.tags, temp_links[i].left_photo.tags)
                right = get_relationship(
                    current_link.left_photo.tags, temp_links[i].right_photo.tags)

                score = 0
                if right > left:
                    score = right
                    left_chain = False
                else:
                    score = left
                    left_chain = True

                if score > max_score:
                    max_score = score
                    best_link = temp_links[i]

            if best_link != None:
                if left_chain:
                    current_link.chain_left(best_link)
                else:
                    current_link.chain_right(best_link)
            else:
                break

            temp_links.remove(best_link)
            new_links.append(current_link)

        links = new_links

        print("\nLinks left: "+str(len(links)) + "          ")

    print("\nDone")
    return links[0].list_of_photos
