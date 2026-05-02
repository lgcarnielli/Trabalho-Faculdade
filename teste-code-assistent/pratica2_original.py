def calc(l):
    s = 0

    for i in range(len(l)):
        s += l[i]

    return s, len(l)


n = [10, 20, 30]

r = calc(n)

print(r)