def get_relationship(tags, tags2):
    left = tags.difference(tags2)
    middle = tags.intersection(tags2)
    right = tags2.difference(tags)

    return min(len(left), len(middle), len(right))

def get_num_intersection(tags, tags2):
    return len(tags.intersection(tags2))
