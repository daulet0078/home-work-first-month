def a_b(a, b):
    c = a + b
    print(c)



def a_b2(a, b):
    c = a + b
    return c

def a_mul_b(a, b):
    c = a * b
    return c


reslt1 = a_b(1, 3)
reslt2 = a_b2(1, 4) - a_mul_b(1, 5)

print(reslt1)
print(reslt2)