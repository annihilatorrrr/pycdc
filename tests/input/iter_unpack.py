def map_with_index(func, lst):
    return [func(i, x) for i, x in enumerate(lst)]
