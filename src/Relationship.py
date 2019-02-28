def get_relationship(tags, tags2):
    left = tags.intersection(tags2)
    middle = tags.union(tags2)
    right = tags.intersection(tags2)

    return min(left.count, middle.count, right.count)
