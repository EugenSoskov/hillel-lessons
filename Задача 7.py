for a in range(1, 20):
    if a == 10:
        print("*")
        break
    else:
        print(" ", end="")
for b in range(8, 1, -2):
    for a in range(1, 20):
        if a == b:
            print("*", end="")

        elif a == 20 - b:
            print("*")
            break
        else:
            print(" ", end="")
for a in range(1, 20):
    if a % 2 != 0:
        print("*", end="")
    else:
        print(" ", end="")
