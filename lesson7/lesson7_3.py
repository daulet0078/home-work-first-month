def a_b2(a, b):
    c = a + b
    return c


def a_sub_b(a, b):
    c = a_b2(a , b) - a_b2(a, b)
    return c

print(a_sub_b(3, 3))