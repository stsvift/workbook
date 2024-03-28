def diff(set1, set2, set3, symmetric=True):
    if symmetric:
        return set_1.symmetric_difference(set_2).symmetric_difference(set_3)
    return set_1.difference(set_2, set_3)

set_1 = {2, 3, 5, 5, 15}
set_2 = {3, 5, 6, 7, 8}
set_3 = {6, 4, 9, 2}


print(diff(set_1, set_2, set_3))
print(diff(set_1, set_2, set_3, symmetric=False))