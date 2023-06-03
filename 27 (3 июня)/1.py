f = list(open('B'))[1:]
m = 0
diff = []
for i in range(len(f)):
    a, b = map(int, f[i].split())
    m += max(a, b)
    diff.append(abs(a - b))
for i in sorted(diff):
    if (m - i) % 33 != 0:
        m -= i
        break
print(m, m % 33)
