def eqv(a, b, c):
    res = a + b
    e = 0.01 / 100
    tolerance = e * max(abs(a), abs(b))
    return abs(res - c) <= tolerance

print(eqv(0.12, 0.31, 0.43))
print(eqv(0.1, 0.2, 0.3))
print(eqv(0.1, 0.2, 0.4))
print(eqv(-0.1, -0.2, -0.3))