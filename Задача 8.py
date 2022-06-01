a = [9, 6, 3, 4, 1, 5, 2, 8, 7]
a.sort(reverse=True)
print(a)
x = int(input("\nВедите число:"))
pos = 0
while pos < len(a) and a[pos] >= x:
    pos += 1
print(pos + 1)
