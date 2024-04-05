my_dict = {'first_one': 'we can do it'}


def biggest_dict(**kwargs):
    my_dict.update(**kwargs)


biggest_dict(k1=22, k2=31, k3=11, k4=91)
biggest_dict(name='Елена', age=31, weight=61, eyes_color='grey')
print(my_dict)