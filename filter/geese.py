def geese_filter(birds):
    subset_of_birds = set(["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"])
    result = [a for a in birds if a not in subset_of_birds]
    return result
