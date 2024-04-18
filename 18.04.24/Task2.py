def mul_to_int(a, b):
    res = a * b
    if float(res).is_integer():
        return int(res)
    return res

print(mul_to_int(2, 4))
print(mul_to_int(2.5, 4))
print(mul_to_int(2.2, 2))