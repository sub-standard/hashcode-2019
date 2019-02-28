def get_relationship(tags, tags2):
    left = tags.difference(tags2)
    middle = tags.intersection(tags2)
    right = tags2.difference(tags)

    return min(len(left), len(middle), len(right))
