from collections.abc import Hashable

def list_to_set(lst):
    st = {item for item in lst if isinstance(item, Hashable)}
    print(st)

list_to_set([1, [2]])
list_to_set([1, [2], 55, 55, {1, 2, 3}, (2, 2), 'string', 5.11])