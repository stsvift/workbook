from collections import Counter
from functools import reduce

dict_1 = {1: 41, 2: 37, 3: 15, 4: 11, 5: 16, 3: 80}
dict_2 = {1: 5, 1: 8, 3: 2, 5: 67, 7: 150}
dict_3 = {3: 5, 3: 8, 4: 70, 6: 50, 7: 52, 8: 11}
dict_4 = {4: 2, 5: 14, 6: 52, 9: 9, 12: 578}

def sum_dct(*dicts):
    return dict(reduce(lambda a, b: Counter(a) + Counter(b), dicts))
def max_dct(*dicts):
    return dict(reduce(lambda a, b: Counter(a) | Counter(b), dicts))
print(max_dct(dict_1, dict_2))
print(sum_dct(dict_1, dict_4, dict_3))
print(max_dct(dict_1, dict_2, dict_3, dict_4))
print(sum_dct(dict_1, dict_2, dict_3, dict_4))