dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

first_key = list(dict.keys())[0]
last_key = list(dict.keys())[-1]
dict[last_key], dict[first_key] = dict[first_key], dict[last_key]

second_key = list(dict.keys())[1]
del dict[second_key]

dict['new_key'] = 'new_value'

print(dict)
