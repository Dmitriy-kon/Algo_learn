a = 50
b = 200

def euclid_nod(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b

print(euclid_nod(a, b))
