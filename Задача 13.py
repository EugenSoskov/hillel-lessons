w = 123405
x = 999
y = 1000
z = 1111


def checkio(integer):
    n = 1
    for i in str(integer):
        t = int(i)
        if t > 0:
            n *= t
    return print(n)


checkio(w)
checkio(x)
checkio(y)
checkio(z)
